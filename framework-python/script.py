#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from streaming.base import BaseMapper, BaseReducer
# from streaming.base import Counter
import time
import urllib
import re
import json


class Mapper(BaseMapper):

    def setup(self):
      pass

    def map(self, key, value):
        try:
            yield value,1
        except Exception:
            print >>sys.stderr, "mapper error line %s" % (sys.exc_info()[1])


class Reducer(BaseReducer):

    def reduce(self, key, values):
        try:
            for value in values:
                yield key,value
        except:
            print >>sys.stderr, "reducer error line %s" % (sys.exc_info()[1])


mapper = Mapper()
combiner = Reducer()
reducer = Reducer()
###############################################################################
# framework (Do Not Modify)
###############################################################################
if __name__ == '__main__':
    from streaming.base import map_reduce_worker
    map_reduce_worker(sys.argv, mapper, reducer, combiner)
