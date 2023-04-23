#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const fs = require('fs');
request.get(args[0], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(args[1], body);
  } else {
    console.log(error);
  }
});
