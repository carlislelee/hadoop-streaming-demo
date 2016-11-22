#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import md5

for line in sys.stdin:
  word = line.strip()
  print '%s\t%s' % (word, str(1))



