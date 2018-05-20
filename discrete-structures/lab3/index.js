'use strict';

function floydWarshall(adjacencyList) {

  for (const k of adjacencyList.keys()) {
    for (const i of adjacencyList.keys()) {
      if (!(adjacencyList.get(k).has(i))) {
        adjacencyList.get(k).set(i, Infinity);
      }
    }
  }

  for (const k of adjacencyList.keys()) {
    for (const i of adjacencyList.keys()) {
      for (const j of adjacencyList.keys()) {
        const ij = adjacencyList.get(i).get(j);
        const ik = adjacencyList.get(i).get(k);
        const kj = adjacencyList.get(k).get(j);
        if (ij && ik && kj) {
          adjacencyList.get(i).set(j, Math.min(ij, ik + kj));
        }
      }
    }
  }

  for (const k of new Array(...adjacencyList.keys()).sort((a, b) => a - b)) {
    for (const i of new Array(
      ...adjacencyList.get(k).keys()).sort((a, b) => a - b)
    ) {
      process.stdout.write((adjacencyList.get(k).get(i) === Infinity ?
        'Inf' : adjacencyList.get(k).get(i)) + '\t');
    }
    console.log();
  }
}

module.exports = floydWarshall;
