from kafka.consumer import KafkaConsumer
from json import loads
from time import sleep
# https://www.youtube.com/watch?v=luiJttJVeBA
import pyspark
# https://github.com/kaantas/kafka-twitter-spark-streaming/blob/master/kafka_twitter_spark_streaming.py

# consumer = KafkaConsumer(
#     'Twitter-Kafka',
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='earliest',
#     enable_auto_commit=True,
#     group_id='my-group-id',
#     value_deserializer=lambda x: loads(x.decode('utf-8'))
# )
#
# for event in consumer:
#     event_data = event.value
#     # Do whatever you want
#     print(event_data)
#     sleep(2)

import sys, os, re, pprint, subprocess
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, Catalog
from pyspark.sql import DataFrame, DataFrameStatFunctions, DataFrameNaFunctions
from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql.types import Row

from subprocess import check_output
# SPARK_DRIVER_HOST = check_output(["hostname", "-i"]).decode(encoding="utf-8").strip()

"""
When deploying a spark application to our cluster configuration we will use three components, a driver, a master, and the workers.

In this case, our driver is your instance of pyspark (same server or remote), our master is spark and our workers are 
spark-worker-1 and spark-worker-2.

So when configuring the snippet we need to ensure the driver can reach the master, the master can reach the driver, 
and workers and master can communicate between them.
- Workers and master will always be able to communicate because they are in the same network and connected via alias 
spark inside docker
- We need to ensure driver/master communication defined in the snippet

"""

# NOTE: Spark driver/client-applications connecting to Spark clusters implemented
# as Docker containers need to set 'spark.driver.host' to be that client's IP-Address,
# not that client's hostname. For example, if launching a PySpark application from your
# desktop, use the desktop's IP-Address. REASON: Because the Docker containers won't have
# an "/etc/hosts" entry for said client (unless you configure it to via docker-compose(5)
# or similar), and so cannot resolve it's (the client's) hostname to communicate back.
# The "SPARK_LOCAL_IP" environment variable is set to that IP-Address as well, so
# that Spark, PySpark, spark-submit(1) don't complain on startup.
# SPARK_MASTER_URL = 'spark://thishost:7077'  # Via "/etc/hosts", name is used here, but IP is recommended.
# ETH0_IP = subprocess.check_output(["hostname", "-i"]).decode(encoding='utf-8').strip()
# ETH0_IP = re.sub(fr'\s*127.0.0.1\s*', '', ETH0_IP)  # Remove alias to 127.0.0.1, if present.
# SPARK_DRIVER_HOST = ETH0_IP
# os.environ["SPARK_LOCAL_IP"] = ETH0_IP

SPARK_DRIVER_HOST = check_output(["hostname", "-i"]).decode(encoding="utf-8").strip()


spark_conf = SparkConf()
spark_conf.setAll([
    ('spark.master', 'spark://spark:7077'), # <--- this host must be resolvable by the driver in this case pyspark (whatever it is located, same server or remote) in our case the IP of server
    ('spark.app.name', 'myApp'),
    ('spark.submit.deployMode', 'client'),
    ('spark.ui.showConsoleProgress', 'true'),
    ('spark.eventLog.enabled', 'false'),
    ('spark.logConf', 'false'),
    ('spark.driver.bindAddress', '0.0.0.0'), # <--- this host is the IP where pyspark will bind the service running the driver (normally 0.0.0.0)
    ('spark.driver.host', SPARK_DRIVER_HOST), # <--- this host is the resolvable IP for the host that is running the driver and it must be reachable by the master and master must be able to reach it (in our case the IP of the container where we are running pyspark
])
# spark_conf.setAll([
#     # this host must be resolvable by the driver in this case pyspark
#     # (whatever it is located, same server or remote), in our case the IP of server
#     ('spark.master', 'spark://172.17.0.6:7077'),
#     ('spark.app.name', 'myApp'),
#     ('spark.submit.deployMode', 'client'),
#     ('spark.ui.showConsoleProgress', 'true'),
#     ('spark.eventLog.enabled', 'false'),
#     ('spark.logConf', 'false'),
#     # this host is the IP where pyspark will bind the service running the driver (normally 0.0.0.0)
#     ('spark.driver.bindAddress', '0.0.0.0'),
#     # this host is the resolvable IP for the host that is running the driver and it must be reachable by the master
#     # and master must be able to reach it (in our case the IP of the container where we are running pyspark
#     ('spark.driver.host', '127.0.1.1'),
# ])

spark_sess = SparkSession.builder.config(conf=spark_conf).getOrCreate()
spark_ctxt = spark_sess.sparkContext
spark_reader = spark_sess.read
# textFile = spark_reader.text("*.md")
# print(textFile.first())
spark_streamReader = spark_sess.readStream
spark_ctxt.setLogLevel("WARN")

myDF = spark_sess.createDataFrame([Row(col0=0, col1=1, col2=2),
                                   Row(col0=3, col1=1, col2=5),
                                   Row(col0=6, col1=2, col2=8)])

myGDF = myDF.select('*').groupBy('col1')
myDF.createOrReplaceTempView('mydf_as_sqltable')
print(myDF.collect())
myGDF.sum().show()
spark_sess.stop()
quit()
