#!/usr/bin/node
/**
 * a script that prints the first argument passed to it
*/

const args = process.argv;

if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}