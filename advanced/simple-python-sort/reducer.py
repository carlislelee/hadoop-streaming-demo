#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys

sort_res = {}

for line in sys.stdin:
  try:
    fields = line.strip().split('\t')
    word = fields[0].split('|')[0]
    if word in sort_res:
      sort_res[word].append(fields[1])
    else:
      sort_res[word] = [fields[1]]
#    sort_res[word] = sort_res.get(word, []).append(fields[1])
    
  except:
    pass


for word in sort_res:
  print '%s\t%s' % (word, sort_res[word])
