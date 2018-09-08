'use strict';

const { treePromise, inorderTraversal } = require(__dirname + '/BST.js');

treePromise.then(sqrtDelete);

function sqrtDelete(tree) {
  for (const i of inorderTraversal(tree.root)) {
    if (Math.sqrt(Math.abs(i)) % 1 === 0) {
      tree.delete(i);
    }
  }
  console.dir(tree, { depth: null });
}
