#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import datetime
#import streaming modules
from streaming.runner import StreamingJob

eggs = [
    'protobuf-2.4.1-py2.7.egg',
    'py_streaming-0.1-py2.7.egg'
]

def run(date_time):
    cmd_env = {'date_time' : date_time}
    #one_day = datetime.timedelta(days=1)
    #one_hour = datetime.timedelta(hours=1)
    job_input = "/home/hdp-ads-audit/user/lizhaoxi/fenxi2.0/mv/src"
    job_output = "/home/hdp-ads-audit/user/lizhaoxi/fenxi2.0/mv/1"
    reducer_num = 2
    load_files = [
        "script.py"
    ]

    StreamingJob(
        script="script.py",
        reducer_num=reducer_num,
        files=load_files,
        cmdenv=cmd_env,
        compress=True,
        use_combiner=False,
        cache_archives={
        },
        eggs=eggs,
        owner="lizhaoxi",
        input=job_input,
        output=job_output,
        job_name='test_201611011523'
    ).run()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >> sys.stderr, "usage: %s time" % (sys.argv[0])
        sys.exit(1)
    date_time = sys.argv[1]
    run(date_time)
