#! /bin/sh

hadoop jar Desktop/LOG8415E/LAB2/hadoop-3.3.1/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar wordcount input output
hdfs dfs -rm output/part-r-00000
hdfs dfs -rm -r output
hadoop jar Desktop/LOG8415E/LAB2/hadoop-3.3.1/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar wordcount input output
hdfs dfs -rm output/part-r-00000
hdfs dfs -rm -r output
hadoop jar Desktop/LOG8415E/LAB2/hadoop-3.3.1/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar wordcount input output
hdfs dfs -rm output/part-r-00000
hdfs dfs -rm -r output
