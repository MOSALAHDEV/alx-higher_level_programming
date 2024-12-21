#!/usr/bin/node
const calcFactorial = parseInt(process.argv[2]);
if (isNaN(calcFactorial) || calcFactorial === 0 || calcFactorial === 1) {
  console.log(1);
} else {
  function fact (n) {
    if (n === 1) {
      return 1;
    } else {
      return n * fact(n - 1);
    }
  }
  console.log(fact(calcFactorial));
}
