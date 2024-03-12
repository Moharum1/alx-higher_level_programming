#!/usr/bin/node
const nums = process.argv.slice(2);

if (nums.length === 0 || nums.length === 1) {
  console.log(0);
} else {
  let biggest = 0;
  nums.forEach(element => {
    if (element > biggest) {
      biggest = element;
    }
  });
  console.log(biggest);
}
