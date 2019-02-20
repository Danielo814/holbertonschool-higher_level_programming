#!/usr/bin/node

const request = require('request');
let url = process.argv[2];
let taskdict = {};
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);
    for (let i = 0; i < tasks.length; i++) {
      let item = tasks[i];
      let user = item.userId;
      let userInDict = taskdict[user];
      if (userInDict === undefined) {
        taskdict[user] = 0;
      }
      if (taskdict[user] !== undefined && item.completed === true) {
        taskdict[user]++;
      }
    }
  } else {
    console.log(error);
  }
  console.log(taskdict);
});
