#!/usr/bin/node
'use strict'
let myArg = process.argv[2];
function factorial (myArg) {
    if (isNaN(myArg) || myArg === 1) {
        return (1);
    } else {
        return (myArg * factorial(myArg - 1));
    }
}
console.log(factorial(parseInt(myArg)));
