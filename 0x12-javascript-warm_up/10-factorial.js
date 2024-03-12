#!/usr/bin/node
const num1 = parseInt(process.argv[2]);

function factorial (a) {
  if (!Number.isInteger(num1) || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

console.log(factorial(num1));
