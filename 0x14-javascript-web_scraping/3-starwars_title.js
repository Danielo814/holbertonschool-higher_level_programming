#!/usr/bin/node

const request = require('request');

let url = 'http://swapi.co/api/films/';

request(url + process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const name = JSON.parse(body);
    console.log(name.title);
  } else {
    console.log(error);
  }
});
