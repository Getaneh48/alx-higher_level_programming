#!/usr/bin/node
/**
 * a script that concats 2 files
 *
 * Note:
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
*/

const fs = require('fs');
const args = process.argv;

for (let i = 2; i <= 3; i++) {
  fs.readFile(args[i], 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      fs.appendFile(args[4], data, (err) => {
        if (err) {
          console.log('erroring writing to a file');
        }
      });
    }
  });
}
