#!/usr/bin/node
const firstArg = process.argv[2];
const message = firstArg === undefined ? 'No argument' : firstArg;
console.log(message);
