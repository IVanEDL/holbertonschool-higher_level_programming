#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
fs.readFile(args[0], 'utf-8', (err, data) => {
    if (err) throw err;
    console.log(data);
  });