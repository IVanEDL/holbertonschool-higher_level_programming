#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tup = (len(sentence), None)
    else:
        tup = (len(sentence), sentence[0])
    return tup
