#!/usr/bin/node

exports.converter = function (base) {
  return function num (n) {
    return n.toString(base);
  };
};
