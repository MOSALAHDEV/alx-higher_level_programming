#!/usr/bin/node
const timesToPrint = parseInt(process.argv[2], 10);
if (isNaN(timesToPrint)) {
  console.log('Missing number of occurrences');
  process.exit(1);
}
for (let i = 0; i < timesToPrint; i++) {
  console.log('C is fun');
}
