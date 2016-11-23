#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys

prev_word = None
word_count = 0

for line in sys.stdin:
  try:
    fields = line.strip().split('\t')
    word = fields[0]
    if word == prev_word:
		word_count += 1
	else:
		if prev_word:
			print '%s\t%s' % (prev_word, word_count)
		word_count = 1
		prev_word = word
  except:
    pass

if prev_word:
	print '%s\t%s' % (prev_word, word_count)
