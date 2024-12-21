#!/usr/bin/node
const calcFactorial = process.argv.slice(2);
if (isNaN(calcFactorial) || calcFactorial === 0 || calcFactorial === 1) {
  console.log(1);
} else {
  let result = 1;
  for (let i = 1; i <= calcFactorial; i++) {
    result *= i;
  }
  console.log(result);
}
