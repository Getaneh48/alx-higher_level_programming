#!/usr/bin/node
/**
 * a script that defines a  function that returns the number of occurrences in a list
*/

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (const item of list) {
    if (item === searchElement) {
      occurence++;
    }
  }
  return (occurence);
};
