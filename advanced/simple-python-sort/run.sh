#!/bin/bash
basedir=$(cd `dirname $0`; pwd)

mapper="mapper.py"
reducer="reducer.py"

input="/home/hdp-ads-audit/user/lizhaoxi/test/secondary_sort/src"
output="/home/hdp-ads-audit/user/lizhaoxi/test/secondary_sort/res"

hadoop fs -rmr $output

hadoop streaming \
  -D mapred.compress.map.output=true \
  -D mapred.map.tasks=3   \
  -D mapred.reduce.tasks=2     \
  -D mapred.job.name="hadoop_streaming_test" \
  -D stream.map.output.field.separator='|'  \
  -D stream.num.map.output.key.fields=4 \
  -D map.output.key.field.separator='|' \
  -D num.key.fields.for.partition=1  \
  -partitioner 'org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner'  \
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

