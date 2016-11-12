#!/usr/bin/env python
# coding=utf-8

def extract_from_tag1(tag,line):
    open = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(open)
        start = i  + len(open)
        j = line.index(closer)
        return line[i:j]
    except ValueRrror:
        return None
def extract_from_tag2(tag,line):
    open = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(open)
        start = i  + len(open)
        j = line.index(closer)
        return line[start:j]
    except ValueRrror:
        return None

print(extract_from_tag1("red","what a <red>rose</red> this is"))
print(extract_from_tag2("red","what a <red>rose</red> this is"))
