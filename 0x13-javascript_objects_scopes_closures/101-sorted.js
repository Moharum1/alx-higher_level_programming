#!/usr/bin/node

const data = require('./101-data').dict;

const mydict = {};

for (const key in data) {
  if (mydict[data[key]] === undefined) {
    mydict[data[key]] = [key];
  } else {
    mydict[data[key]].push(key);
  }
}
console.log(mydict);
