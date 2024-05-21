#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    if (resp.statusCode === 200) {
      const films = JSON.parse(body);
      let count = 0;
      films.results.forEach(film => {
        film.characters.forEach(chr => {
          if (chr.endsWith('/18/')) {
            count++;
          }
        });
      });
      console.log(count);
    }
  }
});
