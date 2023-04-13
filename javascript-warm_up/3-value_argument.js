#!/usr/bin/node
args = process.argv.splice(2);
console.log(args[0] === undefined ? 'No argument' : args[0]);