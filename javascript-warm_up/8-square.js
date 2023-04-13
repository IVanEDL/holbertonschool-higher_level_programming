#!/usr/bin/node
const args = process.argv.slice(2);
const number = parseInt(args[0]);
if (isNaN(number)){
    console.log("Missing size");
} else{
    for(let i = 0; i < number; i++){
        for(let p = 0; p < number; p++){
            process.stdout.write("X");
        }
        process.stdout.write("\n");
    }
}