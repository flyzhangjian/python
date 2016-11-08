#!/usr/bin/env python
# coding=utf-8

import sys

def digit():
    Digits = [["  *** "," *   *","*     *","*     *","*     *"," *   *","  *** "],[" * ","** "," × "," * "," * "," * ","***"]]
    try:
       digits = 2
       row = 0
       while row < 7:
           line = ""
           column = 0
           number = 0
           dddigit = Digits[number]
           while column < len(Digits):
               digit = Digits[column]
               line += digit[row] + " "
               column += 1
           number += 1
           print(line)
           row += 1
    except IndexError:
        print("usage:bigdigits.py <number>")

digit()
