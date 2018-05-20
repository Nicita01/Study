'use strict';

const dir = __dirname;
const KEY_MAX_LENGTH = 20;
const LIMIT_INDEX_OVERLAP = 0.0135;
const RANDOM_TEXT_INDEX_OVERLAP = 0.0501;
const RANDOM_TEXT_INDEX_MUTUAL = 0.0405;
const LIMIT_INDEX_MUTUAL = 0.0195;


const fs = require('fs');
const indexOverlap = require(dir + '/IM.js');
const indMutual = require(dir + '/indexMutualCoincidence.js');
const decoder = require(dir + '/decoder.js');

const textHash = fs.readFileSync(dir + '/codeText.txt', 'utf8').split('');
const samplesObject = {
  [Symbol.iterator]() {
    let curCount = 0;
    return {
      next() {
        curCount++;
        return {
          value: samplesObject[curCount],
          done: curCount === KEY_MAX_LENGTH
        }
      }
    }
  } 
};

for (let keyLength = 1; keyLength <= KEY_MAX_LENGTH; keyLength++) {
  samplesObject[keyLength] = [];
  for (let shift = 0; shift < keyLength; shift++){
    samplesObject[keyLength].push([]);
    for (let cur in textHash) {
      if (((cur) % keyLength === 0) && textHash[parseInt(cur) + shift]) {
        samplesObject[keyLength][shift].push(textHash[parseInt(cur) + shift])
      }
    }
  }
}

const sameIndexOverlapArrays = [];
let cash = [];
for (let curKeyLengthTest of samplesObject) {
  let count = 0;
  let curSum = 0;
  for (let curKeyLengthTestShift of curKeyLengthTest) {
    count++;
    curSum += indexOverlap(curKeyLengthTestShift.join(''));  
  }
  let sum = 0
  let curGlobAvrg = cash.reduce((prev, cur) => {
    return prev + cur
  }, RANDOM_TEXT_INDEX_OVERLAP)/(cash.length + 1);
  let curAvrg = curSum / (count);
  if ( curAvrg > curGlobAvrg + LIMIT_INDEX_OVERLAP ) {
    console.log('length:  ', count);
    sameIndexOverlap(count);
    break;
  } else {
    cash.push(curAvrg);
  }
}


function sameIndexOverlap(keyLength) {
  for (let shift = 0; shift < keyLength; shift++){
    sameIndexOverlapArrays.push([]);
    for (let cur in textHash) {
      if (((cur) % keyLength === 0) && textHash[parseInt(cur) + shift]) {
        sameIndexOverlapArrays[shift].push(textHash[parseInt(cur) + shift]);
      }
    }
  }
  indexMutualCoincidence(sameIndexOverlapArrays)
}

function indexMutualCoincidence(sameIndexOverlapArrays) {
  let shifts = [];
  for (let curShift in sameIndexOverlapArrays) {
    if ( parseInt(curShift) === 0 ) continue;
    let indMutCur = RANDOM_TEXT_INDEX_MUTUAL;
    let cash = [];
    for (let shift = 0; shift < 26; shift++) {
      let cur = sameIndexOverlapArrays[0].map(letter => {
        let charCode = letter.charCodeAt() + shift;
        return String.fromCharCode(charCode > 'z'.charCodeAt() ? charCode - 26 : charCode);
      });
      indMutCur = indMutual(sameIndexOverlapArrays[curShift], cur);
      let indMutAvrg = cash.reduce((prev, cur) => {
        return prev + cur
      }, RANDOM_TEXT_INDEX_MUTUAL)/(cash.length + 1);
      if (indMutCur > indMutAvrg + LIMIT_INDEX_MUTUAL) {
        shifts.push(shift);
        break;
      }
    }
  }
  nameKey(shifts);
}
function nameKey(shifts) {
  let min = 'a'.charCodeAt();
  let max = 'z'.charCodeAt();
  let namesKeyArr = [];
  for ( let cur = min; cur <= max; cur++ ) {
    let first = String.fromCharCode(cur);
    namesKeyArr.push([first]);
    for (let curLet of shifts){
      let code = cur + curLet > 'z'.charCodeAt() ? cur + curLet - 26 : cur + curLet;
      namesKeyArr[cur - 'a'.charCodeAt()].push(String.fromCharCode(code));
    }
  }
  let arrIndexOverlapForKey = []
  for (let curName of namesKeyArr) {
    let y = decoder(textHash.join(''), curName.join('')).join('');
     arrIndexOverlapForKey.push([curName, indMutual(y.split(''), 'e'.split(''))])
  }
  mmax(arrIndexOverlapForKey);
}

function mmax(arrIndexOverlapForKey) {
  let mx = arrIndexOverlapForKey[0][1];
  let c = 0;
  for (let i in arrIndexOverlapForKey) {
    if (arrIndexOverlapForKey[i][1] > mx) {
      mx = arrIndexOverlapForKey[i][1];
      c = i;
    }
  }
  console.log('key:  ', arrIndexOverlapForKey[c][0]);
  const decText = decoder(textHash, arrIndexOverlapForKey[c][0]).join('')
  console.log(
    '\x1b[31mДЕКОДИРОВАННЫЙ ТЕКСТ:\x1b[0m\n', decText);
    fs.writeFileSync(__dirname + '/decodeText.txt', decText, 'utf8');
}
