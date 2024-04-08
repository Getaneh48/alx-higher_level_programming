#!/usr/bin/node
/**
 * a script that prints a square
*/

const arg = parseInt(process.argv[2]);

if (arg) {
  for (let i = 0; i < arg; i++) {
    let str = '';
    for (let j = 0; j < arg; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
