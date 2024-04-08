#!/usr/bin/node
/**
 * a script that prints a message depending of the number of arguments passed
*/

const arglen = process.argv.length;

if (arglen === 2) {
  console.log('No argument');
} else if (arglen === 3) {
  console.log('Argument found');
} else if (arglen > 3) {
  console.log('Arguments found');
}
