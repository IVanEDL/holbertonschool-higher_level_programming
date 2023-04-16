#!/usr/bin/node
const args = process.argv.slice(2);
function add (a, b) {
  const i = parseInt(a) + parseInt(b);
  console.log(i);
}
add(args[0], args[1]);
