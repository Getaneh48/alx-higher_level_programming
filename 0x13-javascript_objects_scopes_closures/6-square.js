#!/usr/bin/node
/**
 * a script that defines a square class
*/

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    let ch = '';
    if (c) {
      ch = c;
    } else {
      ch = 'X';
    }

    for (let i = 0; i < this.width; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += ch;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
