'use strict';

const correct = {
  'q':1, 'w':1, 'e':1, 'r':1, 't':1, 'y':1, 'u':1, 'i':1, 
  'o':1, 'p':1, 'a':1, 's':1, 'd':1, 'f':1, 'g':1, 'h':1, 
  'j':1, 'k':1, 'l':1, 'z':1, 'x':1, 'c':1, 'v':1, 'b':1, 'n':1, 'm':1
};

module.exports = function(text1, text2) {
  let len1 = text1.length;
  let len2 = text2.length;
  return Object.keys(correct).reduce((prev, cur) => {
    let count1 = len1 - text1.join('').split(cur).join('').length;
    let count2 = len2 - text2.join('').split(cur).join('').length;
    let res = count1 * count2 / len1 / len2;
    return prev + res
  }, 0)
}