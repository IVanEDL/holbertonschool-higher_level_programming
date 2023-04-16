#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
        if (!w || !h || w <= 0 || h <= 0) {
            return;
        };
        this.width = w;
        this.height = h;
    };

    print () {
        for (let i = 0; i < this.height; i++) {
            for (let p = 0; i < this.width; p++) {
                process.stdout.write("X");
            };
            process.stdout.write("\n");
        };
    };
};