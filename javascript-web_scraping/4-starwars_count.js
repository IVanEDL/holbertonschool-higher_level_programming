#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
let thatGuy = args[0];
if (args[0] = 'https://swapi-api.hbtn.io/api/films/') {
    thatGuy = 'https://swapi-api.alx-tools.com/api/people/18/';
}
request(thatGuy, (error, response, body) => {
    if (!error && response.statusCode == 200) {
        console.log(JSON.parse(body).films.length);
    }
    else {
        console.log(error);
    }
});
