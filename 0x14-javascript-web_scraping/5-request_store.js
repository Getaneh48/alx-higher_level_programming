#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv;
const url = args[2];
const filename = args[3];

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      } else {
        // display success message
      }
    });
  }
});
