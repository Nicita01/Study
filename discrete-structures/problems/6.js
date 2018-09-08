'use strict';

const { treePromise, inorderTraversal } = require(__dirname + '/BST.js');

const sieveArray = [];
for (let curNumber = 0; curNumber < 100; curNumber++) {
  sieveArray.push(true);
}
sieveArray[0] = false;
sieveArray[1] = false;
for (const curNumber in sieveArray) {
  if (sieveArray[curNumber]) {
    for (let i = parseInt(curNumber) + parseInt(curNumber);
      i < 100; i += parseInt(curNumber)
    ) {
      sieveArray[i] = false;
    }
  }
}

treePromise.then(simpleDelete);

function simpleDelete(tree) {
  for (const i of inorderTraversal(tree.root)) {
    if (sieveArray[Math.abs(i)]) {
      tree.delete(i);
    }
  }
  console.dir(tree, { depth: null });
}
