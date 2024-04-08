#!/usr/bin/node
/**
 * a script that prints the addition of 2 integers
*/

const args = process.argv;

function add (a, b) {
  console.log(a + b);
}

add(parseInt(args[2]), parseInt(args[3]));
