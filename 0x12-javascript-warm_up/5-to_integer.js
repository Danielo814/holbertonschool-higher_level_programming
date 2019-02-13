#!/usr/bin/node
if (isNaN(process.argv[2]) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
