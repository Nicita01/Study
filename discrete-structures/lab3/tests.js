'use strict';

const adjacencyList = new Map();
adjacencyList.set(1, new Map([[1, 0], [2, 3], [3, 8], [5, -4]]));
adjacencyList.set(2, new Map([[2, 0], [4, 1], [5, 7]]));
adjacencyList.set(3, new Map([[2, 4], [3, 0]]));
adjacencyList.set(4, new Map([[1, 2], [3, -5], [4, 0]]));
adjacencyList.set(5, new Map([[4, 6], [5, 0]]));
require(__dirname + '/index.js')(adjacencyList);
