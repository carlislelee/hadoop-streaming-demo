#!/bin/bash
basedir=$(cd `dirname $0`; pwd)

mapper="mapper.py"
reducer="reducer.py"

input="/home/hdp-ads-audit/user/lizhaoxi/test/words"
output="/home/hdp-ads-audit/user/lizhaoxi/test/result"

hadoop fs -rmr $output

hadoop streaming \
  -D mapred.compress.map.output=true \
  -D mapred.map.tasks=3   \
  -D mapred.reduce.tasks=0     \
  -D mapred.job.name="hadoop_streaming_test" \
  -input ${input}                      \
  -output ${output}                    \
  -file $mapper                  \
  -file $reducer                    \
  -mapper $mapper                    \
  -reducer $reducer                     \
  -cmdenv "datekey=20161111"         \

if [ $? -ne 0 ] ; then
  exit 1
fi

