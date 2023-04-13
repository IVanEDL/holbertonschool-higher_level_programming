#!/usr/bin/node
args = process.argv.slice(2);
function add(a, b){
    let i = parseInt(a) + parseInt(b);
    console.log(i);
}
add(args[0], args[1]);