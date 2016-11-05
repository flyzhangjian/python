#!/usr/bin/env python
# coding=utf-8

import re

def build_match_and_apply_functions(pattern,search,replace):
    def matches_rule(word):
        return re.search(pattern,word)

    def apply_rule(word):
        return re.sub(search,replace,word)
    return(matches_rule,apply_rule)

def rule(word):
    rules=[]
    with open('../rules/plural.txt',encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern,search,replace=line.split(None,3)
            rules.append(build_match_and_apply_functions(pattern,search,replace))
    for matches_rule,apply_rule in rules:
        if matches_rule(word):
            return apply_rule(word)

word=input('please input the test word:')
print(rule(word))
