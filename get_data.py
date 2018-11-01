# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:43:17 2018

@author: mingyang.wang
"""

import re
import sys
import unicodedata

def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

# Lowercase, trim, and remove non-letter characters


def normalizeString(s):
    s = unicodeToAscii(s.lower().strip())
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    return s

PATH = "E:\\data\\translate\\cmn-eng\\cmn.txt"
lines = open(PATH, encoding='utf-8').read().strip().split('\n')

cmn = []
eng = []
for l in lines:
    s = l.split('\t')
    s0 = normalizeString(s[0])
    s1 = re.sub('[^\w\u4e00-\u9fff]+', '',s[1])
    eng.append(s0)
    cmn.append(s1)

eng_w = set(" ".join(eng).split(" "))
cmn_w = set("".join(cmn))

eng_w_len = len(eng_w)
cmn_w_len = len(cmn_w)

with open("E:\\data\\translate\\cmn-eng\\data\\cmn.txt","w", encoding='utf8') as f:
    for i in cmn:
        f.write(i)
        f.write("\n")
f.close()
with open("E:\\data\\translate\\cmn-eng\\data\\eng.txt","w") as f:
    for i in eng:
        f.write(i)
        f.write("\n")
f.close()
with open("E:\\data\\translate\\cmn-eng\\data\\cmn_1.txt","w",  encoding='utf8') as f:
    for i in cmn_w:
        f.write(i)
        f.write("\n")
f.close()
with open("E:\\data\\translate\\cmn-eng\\data\\eng_1.txt","w") as f:
    for i in eng_w:
        f.write(i)
        f.write("\n")
f.close()
