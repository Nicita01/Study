'use strict';

const http = require('http');

const server = http.createServer((req, res) => {
  req.on('readable', () => console.log(req.read() + ''));
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.write('datata');
  res.end('END');
}).listen(8000, '127.0.0.1');
