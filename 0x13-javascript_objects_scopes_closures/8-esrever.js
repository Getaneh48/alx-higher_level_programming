#!/usr/bin/node
/**
 * a script that define a function that returns the reversed version of a list
*/

exports.esrever = function (list) {
  const uindex = list.length / 2;
  const len = list.length - 1;

  for (let i = 0; i < uindex; i++) {
    const temp = list[i];
    list[i] = list[len - i];
    list[len - i] = temp;
  }

  return (list);
};
