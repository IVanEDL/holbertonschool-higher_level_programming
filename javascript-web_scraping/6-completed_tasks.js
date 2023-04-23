#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request(args[0], function (error, response, body) {
    if (error) console.log(error);
    const todos = JSON.parse(body);
    const ret = {};
    todos.forEach(function (todo) {
        if (todo.completed === true && !tasks[todo.userId]) {
            tasks[todo.userId] = 1;
        } else if (todo.completed === true && tasks[todo.userId]) {
            tasks[todo.userId] += 1;
        }
    });
    console.log(tasks);
});