#!/usr/bin/node
const item1 = parseInt(process.argv[2]);

if (Number.isInteger(item1)) {
  for (let i = 0; i < item1; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
