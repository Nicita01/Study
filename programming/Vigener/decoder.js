'use strict';

module.exports = function(text, key) {
  let keyArr = [];
  let textArr = [];
  if (typeof(key) === 'string') {
    keyArr = key.split('');
  } else {
    keyArr = key;
  }
  if (typeof(text) === 'string') {
    textArr = text.split('');
  } else {
    textArr = text;
  }
  let codeFirst = keyArr[0].charCodeAt();
  for (let letter in keyArr) {
    if (parseInt(letter) === 0) continue;
    let shift = codeFirst - keyArr[letter].charCodeAt();
    for (let cur in textArr) {
      if ((parseInt(cur)) % key.length === (parseInt(letter))) {
        let code = textArr[parseInt(cur)].charCodeAt() + shift;
        if (code > 'z'.charCodeAt()) code -=26;
        if (code < 'a'.charCodeAt()) code +=26; 
        textArr[cur] = String.fromCharCode(code);
      }
    }
    //console.log('OTL  ', text.join(''));
  }
  let decodingText = textArr.map(value => {
    let curCode = value.charCodeAt() - codeFirst + 'a'.charCodeAt();
    return String.fromCharCode(curCode < 'a'.charCodeAt() ? curCode + 26 : curCode);
  });
  return decodingText;
}


