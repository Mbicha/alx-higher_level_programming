#!/usr/bin/node
'use strict'
let myArgs = process.argv;
let numsList = [];
if (myArgs[2] === undefined || myArgs[3] === undefined){
    console.log(0);
} else {
    for (let i = 2; i < myArgs.length; i++){
        numsList.push(parseInt(myArgs[i]));
    }
    numsList.sort(function (a, b) {return a - b});
    console.log(numsList);
    console.log(numsList[numsList.length-2])
}
