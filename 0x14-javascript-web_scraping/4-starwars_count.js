#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    if (resp.statusCode === 200) {
      const films = JSON.parse(body);
      let count = 0;
      films.results.forEach(film => {
        film.characters.forEach(chr => {
          if (chr === charUrl) {
            count++;
          }
        });
      });
      console.log(count);
    }
  }
});
