#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request(args[0], (error, response, body) => {
    if (error) throw error;
    console.log('code: ' + response.statusCode);
});
