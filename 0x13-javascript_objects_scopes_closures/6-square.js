#!/usr/bin/node
/**
 * a script that defines a square class
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
