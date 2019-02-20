#!/usr/bin/node

const request = require('request');

let id = process.argv[2];
let url = 'https://swapi.co/api/films/';
request(url + id, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body).characters;
    for (let i = 0; i < results.length; i++) {
      request(results[i], function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const name = JSON.parse(body).name;
          console.log(name);
        } else {
          console.log(error);
        }
      });
    }
  } else {
    console.log(error);
  }
});
