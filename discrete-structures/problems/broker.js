'use strict';

const cluster = require('cluster');
const crypto = require('crypto');
// const http = require('http');

// if (cluster.isMaster) {
//   const workers = []
//   for (let i = 0; i < 4; i++) {
//     workers.push(cluster.fork());
//   }
//   const server = http.createServer()
//   workers[2].send('Hello from me outside');
//   workers[2].on('message', (msg) => {console.log(msg + ' FROM CHILD PROCESS id:' +  workers[2].id)});
// } else {
//   console.log = new Proxy(console.log, {
//     apply: (_, __, param) => {
//       require('fs').createWriteStream(__dirname + '/22.txt', 'utf8').write(param + '');
//     }
//   });

//   const container = {};
//   process.on('message', (msg) => {
//     console.log(msg);
//     process.send('HELLO');
//   });
// }

let number = 17;

number = (number + '').split();

let res = 0;

for (const i in number) {
  
  res  = i % 2 === 0 ? res + Math.pow(number[i], 6 - i) : res - Math.pow(number[i], 6 - i);

}

console.log(res);

console.log(crypto.getHashes())