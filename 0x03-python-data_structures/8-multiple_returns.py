#!/usr/bin/python3
def multiple_returns(sentence) -> tuple:
    first_ch = "None"
    if len(sentence) >= 1:
        first_ch = sentence[0]
    return (len(sentence), first_ch)
