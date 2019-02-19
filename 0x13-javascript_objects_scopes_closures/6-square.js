#!/usr/bin/node

const Oldsquare = require('./5-square.js');

module.exports = class Square extends Oldsquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let index = 0; index < this.height; index++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
