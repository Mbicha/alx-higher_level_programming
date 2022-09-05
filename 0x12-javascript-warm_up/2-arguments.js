#!/usr/bin/node
let myArgsLen = process.argv.lenth;
if (myArgsLen === 2)
{
    console.log("No artgument");
}
else if (myArgsLen === 3)
{
    console.log("Argument found");
}
else
{
    console.log("Arguments found");
}
