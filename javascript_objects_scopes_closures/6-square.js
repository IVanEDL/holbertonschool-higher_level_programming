#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square6 extends Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
};
