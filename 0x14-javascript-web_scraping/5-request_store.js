#!/usr/bin/node

const request = require('request');
const fs = require('fs');
let url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8');
  } else {
    console.log(error);
  }
});
