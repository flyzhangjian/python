#!/usr/bin/env python
# coding=utf-8
import sys,unicodedata

def print_unicode_table(word):
    print("decimal hex chr {0:^40}".format("name"))
    print("------------ {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode
    while(code < end):
        c = chr(code)
        name = unicodedata.name(c,"***unknown***")
        if word is None or word in name.lower():
            print("{0:7} {0:5X} {0:^3c} {1}".format(code,name.title()))
        code += 1 

print_unicode_table("0")
