#!/usr/bin/node
/**
 * a script that computes and prints a factorial
*/

const num = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 1) {
    return (n);
  }

  return (n * factorial(n - 1));
}

if (num) {
  const result = factorial(num);
  console.log(result);
} else {
  console.log(1);
}
