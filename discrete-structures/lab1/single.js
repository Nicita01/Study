'use strict';

function LinkedList(...args) {
  this.first = null;
  this.last = null;
  this.length = 0;
  for (const dataChank of args) {
    this.push(dataChank);
  }
}

function Node(data) {
  this.data = data;
  this.next = null;
}

LinkedList.prototype.push = function(data) {
  const node = new Node(data);
  if (!(this.first)) {
    this.first = node;
    this.last = node;
    this.length = 1;
  } else {
    this.last.next = node;
    this.last = node;
    this.length++;
  }
};

LinkedList.prototype.log = function() {
  let curNode = this.first;
  if (curNode) {
    console.log(curNode.data);
  }
  for (let counter = 1; counter < this.length; counter++) {
    curNode = curNode.next;
    console.log(curNode.data);
  }
};

LinkedList.prototype.conditionalCopy = function(condition) {
  const newList = new LinkedList();
  let curNode = this.first;
  for (let counter = 1; counter < this.length; counter++) {
    curNode = curNode.next;
    let conditionOK = true;
    for (const curCondition in condition) {
      if (toString.call(condition[curCondition]).slice(8, -1) === 'RegExp') {
        if (!(condition[curCondition].test(curNode.data[curCondition]))) {
          conditionOK = false;
          break;
        }
      } else if (condition[curCondition] !== curNode.data[curCondition]) {
        conditionOK = false;
        break;
      }
    }
    if (conditionOK) {
      newList.push(curNode.data);
    }
  }
  return newList;
};

// Usage:

const goods = new LinkedList(
  { manufacturer: 'Samsung', name: 'TV 123' },
  { manufacturer: 'SONY', name: 'LKV234' },
  { manufacturer: 'Acer', name: 'Extensa 5683' },
  { manufacturer: 'Asus', name: 'll-46' },
  { manufacturer: 'SONY', name: 'Advance-536' },
  { manufacturer: 'LG', name: 'phone 12' },
  { manufacturer: 'SONY', name: 'DT-111' }
);

const someCondition = goods.conditionalCopy({
  manufacturer: 'SONY', name: /.*/
});
// console.dir(goodsSONY, {depth: null});
someCondition.log();
