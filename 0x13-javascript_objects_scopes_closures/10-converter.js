#!/usr/bin/node
'use strict';
exports.converter = function (base) {
  function conv (number) {
    return number.toString(base);
  }
  return conv;
};
