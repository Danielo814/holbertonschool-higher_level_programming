#!/usr/bin/node

const request = require('request');

let url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    let name = JSON.parse(body).results;
    for (let i = 0; i < name.length; i++) {
      let characters = name[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (name[i].characters[j].indexOf('18') > -1) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
