'use strict';

const NODE_COUNT = 15;

const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const treePromise = new Promise((fn) => {
  rl.question('Введите данные для корневого узла: ', (data) => {
    if (data === '/auto') {
      const tree = new BST(parseInt((Math.random() - 0.5) * 199));
      for (let counter = 1; counter < NODE_COUNT; counter++) {
        const random99 = parseInt((Math.random() - 0.5) * 199);
        tree.add(random99);
      }
      fn(tree);
    } else {
      const tree = new BST(parseInt(data));
      let counter = 1;
      const inputOne = function() {
        rl.question('Введите данные узла: ', (data) => {
          // TODO: Диапаозон -99 - 99
          tree.add(parseInt(data));
          if (counter++ <= NODE_COUNT) {
            inputOne();
          } else {
            fn(tree);
          }
        });
      };
      inputOne();
    }
  });
});

module.exports = { treePromise };

function BST(...args) {
  // TODO: валидация колличества аргументов
  this.root = new Node(args[0]);
  this.count = 1;
  for (const curChunk of args.slice(1)) {
    this.add(curChunk);
  }
}

function Node(data) {
  this.data = data;
  this.left = null;
  this.right = null;
}

BST.prototype.add = function(data) {
  let curNode = this.root;
  while (true) {
    if (curNode.left === null && curNode.data > data) {
      curNode.left = new Node(data);
      this.count++;
      break;
    }
    if (curNode.right === null && curNode.data < data) {
      curNode.right = new Node(data);
      this.count++;
      break;
    }
    if (curNode.data === data) {
      break;
    }
    curNode = curNode[curNode.data > data ? 'left' : 'right'];
  }
};

BST.prototype.delete = function(data) {
  if (this.root.data === data) {
    if (!(this.root.left) && !(this.root.right)) {
      this.root = null;
      this.count--;
      return;
    } else if (!(this.root.left) && this.root.right) {
      this.root = this.root.right;
      this.count--;
      return;
    } else if (this.root.left && !(this.root.right)) {
      this.root = this.root.left;
      this.count--;
      return;
    }
    let curNode = this.root.right;
    if (!(curNode.left)) {
      curNode.left = this.root.left;
      this.root = curNode;
      this.count--;
      return;
    }
    while (true) {
      if (curNode.left.left) {
        curNode = curNode.left;
      } else {
        curNode.left.left = this.root.left;
        const rootRight = this.root.right;
        this.root = curNode;
        curNode.left = curNode.left.right;
        this.root.right = rootRight;
        this.count--;
        return;
      }
    }
  }
  let curNode = this.root;
  while (true) {
    if (curNode.left && curNode.left.data === data) {
      if (!(curNode.left.left) && !(curNode.left.right)) {
        curNode.left = null;
        this.count--;
        return;
      } else if (curNode.left.left && !(curNode.left.right)) {
        curNode.left = curNode.left.left;
        this.count--;
        return;
      } else if (!(curNode.left.left) && curNode.left.right) {
        curNode.left = curNode.left.right;
        this.count--;
        return;
      } else {
        let curNodeSecond = curNode.left.right;
        if (!(curNodeSecond.left)) {
          curNodeSecond.left = curNode.left.left;
          curNode.left = curNodeSecond;
          this.count--;
          return;
        }
        while (true) {
          if (curNodeSecond.left.left) {
            curNodeSecond = curNodeSecond.left;
          } else {
            curNodeSecond.left.left = curNode.left.left;
            const curNodeLeftRight = curNode.left.right;
            curNode.left = curNodeSecond.left;
            curNodeSecond.left = curNodeSecond.left.right;
            curNode.left.right = curNodeLeftRight;
            this.count--;
            return;
          }
        }
      }
    } else
    if (curNode.right && curNode.right.data === data) {
      if (!(curNode.right.left) && !(curNode.right.right)) {
        curNode.right = null;
        this.count--;
        return;
      } else if (curNode.right.left && !(curNode.right.right)) {
        curNode.right = curNode.right.left;
        this.count--;
        return;
      } else if (!(curNode.right.left) && curNode.right.right) {
        curNode.right = curNode.right.right;
        this.count--;
        return;
      } else {
        let curNodeSecond = curNode.right.right;
        if (!(curNodeSecond.left)) {
          curNodeSecond.left = curNode.right.right;
          curNode.right = curNodeSecond;
          this.count--;
          return;
        }
        while (true) {
          if (curNodeSecond.left.left) {
            curNodeSecond = curNodeSecond.left;
          } else {
            curNodeSecond.left.left = curNode.right.right;
            const curNodeRightLeft = curNode.right.left;
            curNode.right = curNodeSecond.left;
            curNodeSecond.left = curNodeSecond.left.right;
            curNode.right.left = curNodeRightLeft;
            this.count--;
            return;
          }
        }
      }
    }
    curNode = curNode[curNode.data > data ? 'left' : 'right'];
  }
};

function* inorderTraversal(curNode) {
  if (curNode) {
    yield* inorderTraversal(curNode.left);
    yield curNode.data;
    yield* inorderTraversal(curNode.right);
  }
}

Object.assign(module.exports, { inorderTraversal });
