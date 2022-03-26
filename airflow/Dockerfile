FROM apache/airflow:2.2.4
USER root
# can also use this to add apt dependencies: build-essential my-awesome-apt-dependency-to-add \

# In order to install packages via apt, you have to switch to root user. Later, we switch back to user airflow.
RUN apt-get update \
  && apt-get install -y openjdk-11-jdk \
  && apt-get install -y ant \
  && apt-get install -y --no-install-recommends \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME; need Java to run Spark. Make sure this version matches the one on Spark
# Currently, we're using Spark:3.1.2 which depends on the JDK build 1.8.0
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

USER airflow

RUN pip install --no-cache-dir apache-airflow-providers-apache-spark
