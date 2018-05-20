'use strict';

const fs = require('fs');
const text = fs.readFileSync(__dirname + '/text.txt', 'utf8');
const correct = {
  'q':1, 'w':1, 'e':1, 'r':1, 't':1, 'y':1, 'u':1, 'i':1, 
  'o':1, 'p':1, 'a':1, 's':1, 'd':1, 'f':1, 'g':1, 'h':1, 
  'j':1, 'k':1, 'l':1, 'z':1, 'x':1, 'c':1, 'v':1, 'b':1, 'n':1, 'm':1
};
console.log('\x1b[31mЗАДАННЫЙ ТЕКСТ:\n\x1b[0m', text)
const goodText = text
  .toLowerCase()
  .split('')
  .filter(cur => cur in correct)
  .join('');
console.log("\x1b[31mТЕКСТ ПРЕОБРАЗОАН В: \n\x1b[0m", goodText);
fs.writeFileSync(__dirname + '/simpleText.txt', goodText, 'utf8');


module.exports = goodText;