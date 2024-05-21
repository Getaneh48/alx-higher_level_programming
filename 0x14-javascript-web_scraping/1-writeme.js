#!/usr/bin/node
const fs = require('fs');

const args = process.argv;
const filename = args[2];
const content = args[3];

fs.writeFile(filename, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  } else {
    // display success message
  }
});
