'use strict';

const fs = require('fs');

const buffer = Buffer.alloc(100);

fs.open(__dirname + '/a.out', 'r', (err, fd) => {
  fs.read(fd, buffer, 0, 100, 0, (err, l) => console.log(buffer.toString()))
})

process.stdout.write('ss');
console.log(12)