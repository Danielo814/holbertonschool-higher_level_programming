#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let arrLength = list.length;
  let count = 0;
  for (let i = 0; i < arrLength; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return (count);
};
