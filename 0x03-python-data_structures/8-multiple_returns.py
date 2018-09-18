#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or len(sentence) < 1:
        return len(sentence), None
    else:
        return len(sentence), sentence[0]
