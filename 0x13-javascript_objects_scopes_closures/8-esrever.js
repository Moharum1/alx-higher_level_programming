#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revlist.push(list[i]);
  }
  return revlist;
};

const esrever = require('./8-esrever').esrever;

console.log(esrever(['1', 2, { id: 3 }, 4, '5', 6]));
