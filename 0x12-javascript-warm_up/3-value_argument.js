#!/usr/bin/node
'use strict'
let myArg = process.argv[2];
if (myArg === undefined){
    console.log("No argument");
} else{
    console.log(myArg);
}
