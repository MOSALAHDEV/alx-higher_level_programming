#!/usr/bin/node
const printSquare = parseInt(process.argv[2], 10);
if (isNaN(printSquare) || printSquare <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < printSquare; i++) {
    console.log('X'.repeat(printSquare));
  }
}
