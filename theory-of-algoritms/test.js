'use strict';

const promise = new Promise((res, rej) => {
  setTimeout(() => rej(new Error()), 1000);
});

promise
  .catch(err => console.log(1 + err))
  .then(res => console.log(2), rej => console.log(3 + rej));