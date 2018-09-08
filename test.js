'use strict';

const db = require('mongodb').MongoClient;
// console.log(db);

db.connect('mongodb://localhost:27017/test', (err, dd) => {
  const db = dd.db('test');
  const collect = db.collection('first');
  collect.insert({ info: 'value' }, (err, res) => {
    console.log(res);
  });
  // console.log(collect.find('a')); //({'a': 1});
  collect.findOne().then((value) => console.log(value))
  dd.close();
})