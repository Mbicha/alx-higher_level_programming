#!/usr/bin/node
let myArgs = process.argv;
function add(a, b){
    return (a + b);
}
if (isNaN(myArgs[2]) || isNaN(myArgs[3])){
    console.log("NaN");
} else {
    console.log(add(parseInt(myArgs[2]), parseInt(myArgs[3])));
}
