#!/usr/bin/node
const args = process.argv.slice(2)
console.log(args.length === 0 ? 'No argument' : args.length === 1 ? 'Argument found' : 'Arguments found');