#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys

word_count = {}

for line in sys.stdin:
  try:
    fields = line.strip().split('\t')
    word = fields[0]
    word_count[word] = word_count.get(word, 0) + 1
    
  except:
    pass


for word in word_count:
  print '%s\t%s' % (word, word_count[word])
