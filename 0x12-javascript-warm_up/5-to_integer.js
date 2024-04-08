#!/usr/bin/node
/**
 * a script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
*/

const args = process.argv;
const val = parseInt(args[2]);

if (val) {
  console.log(`My number: ${val}`);
} else {
  console.log('Not a number');
}
