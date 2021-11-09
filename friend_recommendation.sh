#! /bin/bash

hdfs dfs -rm -r /input
hdfs dfs -rm -r /output
hdfs dfs -mkdir /input
hdfs dfs -put soc-LiveJournal1Adj.txt /input
mapred streaming -Dmapreduce.job.maps=1 -input /input -output /output -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py
hdfs dfs -get /output/part-00000
cat part-00000 > friend_recommendation_final.txt
rm part-00000
