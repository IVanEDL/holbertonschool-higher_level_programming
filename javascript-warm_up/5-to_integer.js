#!/usr/bin/node
const args = process.argv.splice(2);
const number = parseInt(args[0]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
