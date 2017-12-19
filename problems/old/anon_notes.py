#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author Kevin Taha
# @version 10-12-2017

# Notes: Converts both strings into arrays because strings are immutable and arrays are not.
# Did that in one line for fun and to learn fancy Python stuff at the cost of readability.
# Sort of brute forced through arrays. Removing to deal w/ duplicate words.
# This solution would break with punctuation.
def anon_note_checker(text, message):
    textwords, messagewords = map(lambda x: x.lower().split(), [text, message])
    for i in messagewords:
        if i in textwords:
            textwords.remove(i)
        else:
            return False
    return True



# Notes: This solution works with all non-alphabetic characters by separating them
# from the string before splitting. Not entirely an efficient process and it doesn't
# play nicely w/ test cases but it works ¯\_(ツ)_/¯
def separate_punct(text):
        for i in text:
            if not i.isalpha():
                text = text.replace(i, " " + i + " ")
        return text
def anon_note_checker_plus(text, message):
    text = separate_punct(text).lower().split()
    message = separate_punct(message).lower().split()
    for i in message:
        if i in text:
            text.remove(i)
        else:
            return False
    return True
# print anon_note_checker_plus("Hello? World!", "HeLlo world!")
