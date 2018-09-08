'use strict';

const im = function(text) {
  const correct = {
    'q':1, 'w':1, 'e':1, 'r':1, 't':1, 'y':1, 'u':1, 'i':1, 
    'o':1, 'p':1, 'a':1, 's':1, 'd':1, 'f':1, 'g':1, 'h':1, 
    'j':1, 'k':1, 'l':1, 'z':1, 'x':1, 'c':1, 'v':1, 'b':1, 'n':1, 'm':1
  };
  const all = text.length;
  let im = 0;
  for (let curLetter in correct) {
    im += Math.pow((all - text.split(curLetter).join('').length)/all, 2);
  }
  return im;
}
module.exports = im