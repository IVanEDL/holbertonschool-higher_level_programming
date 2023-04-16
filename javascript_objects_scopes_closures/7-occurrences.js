#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let i = 0;
    for (const p in list) {
        if (list[p] === searchElement) {
            i += 1;
        }
    }
    return i;
};