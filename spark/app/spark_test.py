# import sys, os
# from pyspark.conf import SparkConf
# from pyspark.sql import SparkSession
# from pyspark.sql.types import Row
# from subprocess import check_output

import pyspark
sc = pyspark.SparkContext(appName="test")
print(sc.range(100).count())

# spark_conf = SparkConf()
#
#
# # SPARK_DRIVER_HOST = '172.28.0.2' # WHEN RUNNING FROM WITHIN DOCKER CONTAINER
# # SPARK_DRIVER_HOST = '127.0.0.1' # LOCALHOST
# SPARK_DRIVER_HOST = check_output(["hostname", "-i"]).decode(encoding="utf-8").strip()
#
# # docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name_or_id> [quantropy-spark-1]
# SPARK_MASTER_IP = '172.28.0.6' # IP ADDRESS OF SPARK MASTER INSIDE DOCKER SERVICE
#
# spark_conf.setAll(
#     [
#         ("spark.master", f"spark://spark-master:7077",),
#         ("spark.app.name", "myApp"),
#         ("spark.submit.deployMode", "client"),
#         ("spark.ui.showConsoleProgress", "true"),
#         ("spark.eventLog.enabled", "false"),
#         ("spark.logConf", "false"),
#         ("spark.driver.bindAddress", "0.0.0.0"),
#         ("spark.driver.host", SPARK_DRIVER_HOST)
#     ]
# )
#
# spark_sess = SparkSession.builder.config(conf=spark_conf).getOrCreate()
# spark_reader = spark_sess.read
#
# myDF = spark_sess.createDataFrame(
#     [
#         Row(col0=0, col1=1, col2=2),
#         Row(col0=3, col1=1, col2=5),
#         Row(col0=6, col1=2, col2=8),
#     ]
# )
#
# myGDF = myDF.select("*").groupBy("col1")
# myDF.createOrReplaceTempView("mydf_as_sqltable")
# print(myDF.collect())
# myGDF.sum().show()
#
# spark_sess.stop()
quit()