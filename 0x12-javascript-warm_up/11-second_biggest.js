#!/usr/bin/node
/**
 * a script that searches the second biggest integer in the list of arguments
*/

const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  let list = args.slice(2, args.length);
  list.sort().reverse();
  list = [...new Set(list)];
  console.log(list[1]);
}
