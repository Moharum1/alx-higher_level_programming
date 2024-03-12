#!/usr/bin/node
const item = process.argv[2];

if (typeof (item) === 'undefined') {
  console.log('No argument');
} else {
  console.log(item);
}
