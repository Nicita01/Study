'use strict';

const http = require('http');
const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

function input() {
  rl.question('Введите шифр:', (preHash) => {
    rl.question('Введите данные:', (data) => {
      // соединение с сервером и отправка на брокер
      if (preHash !== '/exit') input();
    });
  });
}

function sending() {
  
}

const options = {
  hostname: '127.0.0.1',
  port: 8000,
  method: 'POST',
  headers: {
    'Content-Type': 'text/plain',
    'Content-Length': 2,
    'encoding': 'utf8'
  },
};

let req = http.request(options, (res) => {
  res.setEncoding('utf8');
  res.on('data', (chunk) => {console.log(`BODYY: ${chunk + ''}`);});
  res.on('end', () => {console.log('No more data in response.');});
});

req.write('1asd');
req.write('2asd');
setTimeout(() => {req.write('wer'); req.end();}, 100)
