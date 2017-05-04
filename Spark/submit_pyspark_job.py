# create a python script using vi/vim
# run the script using submit command as below
# spark-submit --master yarn submit_pyspark_job.py

from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("pyspark")

sc = SparkContext(conf = conf)

dept = sc.textFile("/user/cloudera/sqoop_import/departments")

for line in dept.collect():
   print(line)

dept.saveAsTextFile("/user/cloudera/pyspark/departments")