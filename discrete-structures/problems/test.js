'use strict';

// const cluster = require('cluster');

// if (cluster.isMaster) {
//   // Fork workers.
//   cluster.fork();
//   cluster.fork();
//   cluster.on('disconnect', (ww) => console.log(ww.id))
 
// } else {
//   // Workers can share any TCP connection
//   // In this case it is an HTTP server

//   // http.createServer((req, res) => {
//   //   res.writeHead(200);
//   //   res.end('hello world\n');
//   // }).listen(8000);
//   setTimeout(() => {
//     if (cluster.worker.id % 2 === 0) {
//       cluster.worker.kill();
//     }
//   }, 2000);
// }
// /

process.on('exit', () => {
  setTimeout(() => {
    console.log(11);
  }, 2000);
});
