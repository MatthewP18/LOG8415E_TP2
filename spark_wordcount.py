import pyspark
import timeit
sc = pyspark.SparkContext('local[*]')

words1 = sc.textFile('file:////home/arthur/spark/buchanj-midwinter-00-t.txt').flatMap(lambda line: line.split(' '))
words2 = sc.textFile('file:////home/arthur/spark/carman-farhorizons-00-t.txt').flatMap(lambda line: line.split(' '))
words3 = sc.textFile('file:////home/arthur/spark/colby-champlain-00-t.txt').flatMap(lambda line: line.split(' '))
words4 = sc.textFile('file:////home/arthur/spark/cheyneyp-darkbahama-00-t.txt').flatMap(lambda line: line.split(' '))
words5 = sc.textFile('file:////home/arthur/spark/delamare-bumps-00-t.txt').flatMap(lambda line: line.split(' '))
words6 = sc.textFile('file:////home/arthur/spark/charlesworth-scene-00-t.txt').flatMap(lambda line: line.split(' '))
words7 = sc.textFile('file:////home/arthur/spark/delamare-lucy-00-t.txt').flatMap(lambda line: line.split(' '))
words8 = sc.textFile('file:////home/arthur/spark/delamare-myfanwy-00-t.txt').flatMap(lambda line: line.split(' '))
words9 = sc.textFile('file:////home/arthur/spark/delamare-penny-00-t.txt').flatMap(lambda line: line.split(' '))



wordCounts1 = words1.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
wordCounts2 = words2.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
wordCounts3 = words3.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
wordCounts4 = words4.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
wordCounts5 = words5.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
wordCounts6 = words6.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
wordCounts7 = words7.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
wordCounts8 = words8.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
wordCounts9 = words9.map(lambda word: (word, 1)).reduceByKey(lambda a, b:a +b)
