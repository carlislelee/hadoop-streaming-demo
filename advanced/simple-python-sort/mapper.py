#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys

for line in sys.stdin:
  word,val = line.strip().split(' ',1)
  #print len(fs)
  print '%s\t%s' % (word + '|' + val, val)



