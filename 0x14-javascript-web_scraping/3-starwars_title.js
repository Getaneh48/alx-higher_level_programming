#!/usr/bin/node
const request = require('request');

const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
