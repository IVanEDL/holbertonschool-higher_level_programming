#!/usr/bin/node
exports.esrever = function (list) {
    const tsil = [];
    let i = 0;
    for (let p = list.length - 1; p <= 0; p--) {
        tsil[i] = list[p];
        i++;
    }
    return tsil;
};