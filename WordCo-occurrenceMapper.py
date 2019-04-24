#!/usr/bin/env python
"""mapper.py"""
import sys,re
from itertools import combinations

for line in sys.stdin:
     keyWords = {'basketball': 0, 'team': 0, 'game': 0, 'coach': 0, 'college': 0, 'ncaa': 0, 'will': 0, 'tournament': 0,'year': 0, 'play': 0}
     result = []
     line = re.sub("[^a-zA-Z-0-9]", " ", line)
     line = line.strip()
     words = line.split()
     for word in words:
         if word in keyWords.keys():
             keyWords[word]+=1
     for element,count in keyWords.items():
         if count>=1:
             result.append(element)
     comb = combinations(result,2)
     for x in comb:
         a = x[0].encode("utf-8")
         b = x[1].encode("utf-8")
         print '(%s,%s)\t%s' % (a,b,1)



