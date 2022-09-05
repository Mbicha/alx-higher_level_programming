#!/usr/bin/node
let myArg = process.argv[2];
let myString = "C is fun";
if(isNaN(myArg)){
    console.log("Missing number of occurrences");
}else{
    while (myArg > 0) {
        console.log(myString);
        myArg--;
    }
}
