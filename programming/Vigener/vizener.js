'use strict';

const goodText = require(__dirname + '/simleText.js').split('');
const readline = require("readline");
const fs = require("fs");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Введите ключевое слово:\n", (salt) => {
  fs.writeFileSync(
    __dirname + "/codeText.txt", 
    chipher(salt).join(''), 
    'utf8'
  );
  console.log('\x1b[31mТЕКСТ ЗАШИФРОВАН В \x1b[36m/codeText.txt\x1b[0m');
});

function chipher(salt) {
  return goodText.map((cur, index) => {
    const chipN = cur.charCodeAt() + salt[index % salt.length].charCodeAt() - 'a'.charCodeAt();
    return String.fromCharCode(chipN > 'z'.charCodeAt() ? chipN - 26 : chipN);
  });
}


