#!/usr/bin/node
let myArg = process.argv[2];
if (isNaN(myArg)){
    console.log("Missing size");
} else {
    for (let i = 0; i < myArg; i++){
        console.log("X".repeat(myArg));
    }
}
