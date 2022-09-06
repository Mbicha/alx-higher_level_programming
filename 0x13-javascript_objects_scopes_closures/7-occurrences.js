#!/usr/bin/node
'use strict';
exports.nbOccurences = function (list, searchElement) {
  let countElement = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      countElement++;
    }
  }
  return countElement;
};
