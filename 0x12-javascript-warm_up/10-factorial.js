#!/usr/bin/node
function factorial (i) {
  let x = parseInt(i);
  if (isNaN(x) || x === 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(factorial(process.argv[2]));
