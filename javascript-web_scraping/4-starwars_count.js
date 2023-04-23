#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
let thatGuy = args[0];
if (args[0] === 'https://swapi-api.hbtn.io/api/films/') {
  thatGuy = 'https://swapi-api.alx-tools.com/api/people/18/';
}
request.get(thatGuy, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body).films.length;
    console.log(data);
  } else {
    console.log(error);
  }
});
