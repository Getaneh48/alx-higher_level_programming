#!/usr/bin/node
const request = require('request');

const args = process.argv;
const url = args[2];

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${resp.statusCode}`);
  }
});
