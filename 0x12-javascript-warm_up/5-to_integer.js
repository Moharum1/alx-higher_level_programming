#!/usr/bin/node
const item1 = parseInt(process.argv[2]);
if (Number.isInteger(item1)) {
  console.log('My number:', item1);
} else {
  console.log('Not a number');
}
