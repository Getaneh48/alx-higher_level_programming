#!/usr/bin/node
/**
 * a script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence
*/

const dict = require('./101-data').dict;

const vals = [...new Set(Object.values(dict))]; // get the dict values and remove duplicates
const newDict = {};
let group = [];

for (const val of vals) {
  group = [];
  for (const key of Object.keys(dict)) {
    if (dict[key] === val) {
      group.push(key);
    }
  }
  newDict[val] = group;
}

console.log(newDict);
