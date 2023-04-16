#!/usr/bin/node
const args = process.argv.slice(2);
function factorio (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  }
  return x * factorio(x - 1);
}
console.log(factorio(args[0]));
