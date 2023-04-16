#!/usr/bin/node
exports.esrever = function (list) {
    const tsil = [];
    for (let i = 0, p = list.length - 1; p <= 0; p--) {
        tsil[i] = list[p];
        i++;
    }
    return tsil;
};