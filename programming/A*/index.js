'use strict';

const makeGraph = require(__dirname + '/graph-maker');
const Heap = require(__dirname + '/binary-heap.js');

const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const dataStrArr = require('fs')
  .readFileSync(__dirname + '/input.txt')
  .toString()
  .split('\n');

const strCount = dataStrArr.length;
let maxCountColumn = dataStrArr[0].length;
for (const curStr in dataStrArr) {
  maxCountColumn = Math.max(maxCountColumn, curStr.length);
}
process.stdout.write(' '.repeat((strCount + '').length + 1));
for (let curSymb = 0; curSymb < maxCountColumn; curSymb++) {
  process.stdout.write(String.fromCharCode('A'.charCodeAt() + curSymb));
}
process.stdout.write('\n');
for (const curString in dataStrArr) {
  console.log(curString +
    ' '.repeat((strCount + '').length + 1 - curString.length) +
    dataStrArr[curString]
      .replace(/[^1234567890 ]/g, 'x')
      .replace(/[1234567890 ]/g, '-')
  );
}


const dataArr = dataStrArr.map(curStr => curStr.split('').map(
  curSymb => (parseInt(curSymb) == curSymb ? parseInt(curSymb) : curSymb)
));
const graphFoundation = makeGraph(dataArr);
rl.question('Введите координаты начала пути (в формате A0): ', (start) => {
  const startX = start.charCodeAt() - 'A'.charCodeAt();
  const startY = parseInt(start.slice(1));
  if (!(graphFoundation[startY]) || !(graphFoundation[startY][startX])) {
    throw {
      message: 'Вы не можете стартовать с этой точки',
      name: 'LogicError'
    };
  }
  rl.question('Введите координаты цели: ', (finish) => {
    rl.close();
    const finishX = finish.charCodeAt() - 'A'.charCodeAt();
    const finishY = parseInt(finish.slice(1));
    const startNode = graphFoundation[startY][startX];
    startNode.length = startNode.complexity;
    aStar(startNode, finishX, finishY);
    output(graphFoundation);
  });
});

function aStar(startNode, finishX, finishY) {
  const heap = new Heap([0, startNode]);
  let curNode;
  while (heap.root) {
    curNode = heap.get();
    if (curNode.x == finishX && curNode.y == finishY) {
      reverseRound(curNode);
      return;
    }
    for (const curNeighbor of curNode.newNeighbors()) {
      const newCost = curNode.length + curNeighbor.complexity;
      if (newCost < curNeighbor.length) {
        curNeighbor.length = newCost;
        curNeighbor.wentFrom = curNode;
        const distanse =
          Math.abs(curNeighbor.x - finishX) + Math.abs(curNeighbor.y - finishY);
        heap.add(distanse + newCost, curNeighbor);
      }
    }
  }
  throw {
    message: 'Путь построить нельзя',
    name: 'LogicError'
  };
}

function reverseRound(finishNode) {
  let curNode = finishNode;
  while (curNode) {
    curNode.complexity = '\x1b[32m' + curNode.complexity;
    curNode = curNode.wentFrom;
  }
}

function output(graphFoundation) {
  for (const curStr in graphFoundation) {
    for (const curColumn in graphFoundation[curStr]) {
      if (graphFoundation[curStr][curColumn]) {
        process.stdout.write(
          graphFoundation[curStr][curColumn].complexity + ''
        );
        process.stdout.write('\x1b[0m');
      } else {
        process.stdout.write('\x1b[31m' + dataArr[curStr][curColumn]);
        process.stdout.write('\x1b[0m');
      }
    }
    process.stdout.write('\n');
  }
}
