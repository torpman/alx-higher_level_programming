#!/usr/bin/python3
def multiple_returns(sentence):
    sentenceLen = len(sentence)
    if sentenceLen == 0:
        return sentenceLen, None
    return sentenceLen, sentence[0]
