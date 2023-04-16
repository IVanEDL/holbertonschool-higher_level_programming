#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  for (let p = list.length - 1, i = 0; p >= 0; p--) {
    tsil[i] = list[p];
    i++;
  }
  return tsil;
};
