Resources:
* https://github.com/josephmachado/beginner_de_project

* https://dev.to/mvillarrealb/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-2021-update-6l4

* https://dtuto.com/questions/2314/modulenotfounderror-no-module-named-airflow-providers-apache
* https://stackoverflow.com/questions/67851351/cannot-install-additional-requirements-to-apache-airflow
* https://github.com/dsaidgovsg/airflow-pipeline
* https://github.com/cordon-thiago/airflow-spark [check everything actually. also check the dags for integration with DB and csv's]
* twitter with kafka/spark streaming: https://github.com/kaantas/kafka-twitter-spark-streaming
* add dev and prod environments: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
* Airflow, Spark, Jupyter: https://medium.com/data-arena/building-a-spark-and-airflow-development-environment-with-docker-f0b9b625edd8
* https://github.com/DataTalksClub/data-engineering-zoomcamp
* https://github.com/abhishek-ch/around-dataengineering

Airflow:
* Python 3.7
* JDK 11

Spark: latest
* Python 3.8
* JDK 8

Spark: 3.1.2
* Python: 3.6
* JDK 1.8

This environment comes with Python & PySpark support, as well as pip and conda so that it's easy to to install additional Python packages.



Driver, Host, IP, Port

# Overview

Raison d’être: Let's be real. You can count on your fingers the people who enjoy setting up their development environments; 
whether it's the daunting bash scripts, `$HOME` environment variables, dependencies circular hell; 

Modern Data Stack. 
We understand there is no one-size-fits-all solution, that tools come and go but the underlying principles remain. 


Setting Good Practices.
* **Low-code / No-code:** While I don't particularly advocate for this movement, 

Docker: enables system administrators and developers to build distributed applications.
## On the Shoulder of Giants

This is what I aim to provide in this repository
* **Layer 1 | Data as a Service:** Ready-made ETL mechanisms for common use cases that we can provide to clients to build their models on. 
Mutual agreement
* **Layer 2 | Model as a Service:** Client trains their own . 
* **Layer 3**

We allow for different architectures based on your use-cases, and combinations thereof
* Support for both Data Warehouses and Data Lakes.
* Support for both ETL and ELT pipelines.
* Support for both OLAP and OLTP.
* Support for both Stream and Batch processing.

Finally, they contain a combination of versions from the components listed below. Note that not all the combination exist. 
Feel free to specify them in the `.env` file.

| Service    | Function | Image | Versions Available| Env Variabe | Host/Port      |
|------------|----------|-------|--------------------|------------|----------------|
| PostgreSQL | RDBMS    || [localhost:5432](localhost:5432) |
| Airflow    | Data Workload Scheduler & Orchestrator| [localhost:8080](localhost:8080)||||

If at any point, you believe you messed up with versioning and need to roll-back, use the `docker-compose down --volumes --rmi all` command, then re-run your original commands.

We have support for the following:
* **Cloud Providers:** AWS (Amazon), Azure (Microsoft), GCP (Google).
* **Data Warehousing:** Redshift, Snowflake, BigQuery.
* **Data Lakes:** Delta Lake, AWS S3 (`s3a://`), Google Cloud Storage (`gs://`), Azure Blob Storage (`wasbs://`), 

## Extracting Data

HTTP(S), FTP, TCP, GRPC, REST, WebSocket

We collect data from sources such as governmental websites, social media...


### APIs
- Social Media: Twitter, Reddit
- Governmental: StatsCan

### Crawling & Scraping
- SEC

### Transfer Protocols
Think MFT, FTP, SFTP
## Loading / Storing Data

## Processing / Transforming Data

## Visualizing Data

# Components of our Architecture

Below we explain 



# Package Dependency Management
* pip
* Anaconda
* Poetry

# Sphinx | Documentation Generator

# Airflow | Scheduler & Orchestrator

First, we initialize Airflow's database; we need to run database migrations and create the first user account for Airflow.
```
> docker-compose up airflow-init
```
You should see
```
airflow-init_1       | User "airflow" created with role "Admin"
airflow-init_1       | 2.2.4
```

We extend Bitmami's Airflow image capabilities with our own, specifically by creating a new `Dockerfile` with the following content.

```
FROM apache/airflow:2.0.0
RUN pip install --no-cache-dir apache-airflow-providers-apache-spark
```

Then, we build the new image

```commandline
docker build ./airflow --tag dunya-airflow:2.2.4
```

We then set this image in `docker-compose.yaml` file, using its tag:

```
echo "AIRFLOW_IMAGE_NAME=dunya-airflow:2.2.4" >> .env
```

Now, under `x-airflow-common` in the `docker-compose.yaml`, we can use this image through the environment variable,
 as follows: `image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.2.4}`. So it'll look for the `AIRFLOW_IMAGE_NAME` in your environment 
 variables, and if it doesn't find one defined, it defaults to the `apache/airflow:2.2.4` image.

Instead of building the image manually, you can also simply replace the `image` option with a `build` under `x-airflow-common`, in order to build your Airflow's image, and giving its path; 
specifically, `build: ./airflow`, if you're sure you want to use your own Airflow image and avoid defaulting to Bitnami's (the original image).

As for the `airflow.cfg` file, we don't actually need one since we can set any option that exists in `airflow.cfg` by using environment variables following this syntax `AIRFLOW__{SECTION}__{KEY}` under `&airflow-common-env` in our `docker-compose.yaml`.
You can also modify the `docker-compose` directly for installing some dependencies [instead of doing it via the Dockerfile], specifically by adding 
the environment variable `_PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:- package1 package2 package3 }`. This way, you can add other providers' libraries such as Spark, Oracle, MS SQL... For example, `_PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:- apache-airflow-providers-apache-spark apache-airflow-providers-oracle apache-airflow-providers-microsoft-mssql}`. 
However, I opted for the former option of extending the original Airflow image (Bitnami's) with other `apt` and `pip` 
dependencies (under `./airflow`)in order to make our image more extensible.

Now, run the rest of the services using `docker-compose up -d`. 

# Django + React | Backend & Frontend App

you can run the `web` service to create a Django project
```
# The following command instructs compose to run django-admin startproject composeexample in a container, 
# using the web service’s image and configuration. 
> docker-compose run web django-admin startproject dunya_app .
```

* Dev and test environments
* Gunicorn and Nginx for Production environment

# Postgres | RDBMS

We want to run the command as the postgres user because the docker exec command defaults 
to using the root user and the root user does not have access to the database.

```> docker exec -it dunya-postgres-1 psql -U airflow```

Then, inside the container
```
# psql -h localhost -p 5432 -U docker -d docker
List: To list all databases
# \l
Connection: To view which database you're connected do, and as which user
# \c
To connect to a certain database, `# \c <db_name>`
To display all tables in the database
# \dt
```

# MongoDB | NoSQL Database

# Kafka | Message Broker

# Spark | Large-Scale Data Processor

As for Spark, we need to write our own image. In fact, while Airflow's image runs on Python 3.7 and JDK 11, 
Spark's (even latest version) runs on JDK 8, causing incompatibility issues.

```
docker build ./spark --tag cluster-apache-spark:3.0.2
```

The same Python version needs to be used on the driver (airflow in this case) and on the Spark workers. 
The python version used at driver and worker side can be adjusted by setting the environment variables 
PYSPARK_PYTHON and / or PYSPARK_DRIVER_PYTHON, see Spark Configuration for more information.

To run a standalone Spark job, we'll present three alternatives I've commonly seen

**Alternative 1:** Run a docker service (specifying the volume mounting and network connection), 
then run your Spark job (in this case `spark_test.py`) from within that service, using 
```
docker run --rm -ti --name devtest -u root -v ${pwd}/spark_test.py:/bitnami/spark/spark_test.py --network quantropy_default_net bitnami/spark:3-debian-10 bash
cd /bitnami/spark
pip install pyspark
python spark_test.py
```
**Alternative 2:** More conveniently, you can also make a service out of it and add it in your `docker-compose`:

```yaml
work-env:
    image: docker.io/bitnami/spark:3.1.2
    volumes:
      - ./spark/app:/usr/local/spark/app
    command: tail -f /dev/null
    user: root
    working_dir: /usr/local/spark/app
    environment: # $SPARK_HOME is /opt/bitnami/spark
      PYTHONPATH: /opt/bitnami/spark/python:/opt/bitnami/spark/python/lib/py4j-0.10.9-src.zip
    depends_on:
      - spark-master
```
**Alternative 3:** Most simply, just use the `spark-submit` operator within `spark-master`; 
```
docker exec spark-master spark-submit --master spark://spark-master:7077 /usr/local/spark/app/spark_test.py
```

You can also scale the number of spark workers (same idea as kafka brokers). 

**Alternative 1:**
```
> docker-compose up --scale spark-worker=3 -d
```
**Alternative 2:** You can add workers copying the containers and changing the container name inside the docker-compose.yml file.

### Scheduling Spark jobs with our orchestrator Airflow

airflow.cfg: https://github.com/puckel/docker-airflow/issues/571#issuecomment-845514720
copy airflow.cfg into spark/app/resources/data

You can run a Spark Job using airflow config using (TO-DO): 
```
docker exec -it dunya_airflow-webserver_1 spark-submit --master spark://spark-master:7077 /usr/local/spark/app/hello-world.py /usr/local/spark/resources/data/airflow.cfg
```

You should be able to see the result of the job in the output:

```
22/03/23 22:25:05 INFO TaskSchedulerImpl: Killing all running tasks in stage 1: Stage finished
22/03/23 22:25:05 INFO DAGScheduler: Job 1 finished: count at /usr/local/spark/app/hello-world.py:26, took 0.141446 s
Lines with a: 653, lines with b: 309
```
Alternatively, you can run Spark jobs in Airflow via Airflow's UI. On the top bar, go to Admin -> Connections.
Add a connection and fill the following fields' values: 
* **Connection Id:** spark_default
* **Connection Type:** Spark
* **Host:** `spark://spark-master`
* **Port:** 7077

Alternatively,

``` TODO
docker exec -d beginner_de_project_airflow-webserver_1 airflow connections add 'redshift' --conn-type 'Postgres' --conn-login $REDSHIFT_USER --conn-password $REDSHIFT_PASSWORD --conn-host $REDSHIFT_HOST --conn-port $REDSHIFT_PORT --conn-schema 'dev'
```

### Running Spark jobs in Jupyter

### Processing data stored in Data Warehouses
* Snowflake

### Processing data stored in Delta Lakes

Our images come built-in with connectors to common data sources:

* AWS S3 ( s3a://)
* Google Cloud Storage ( gs://)
* Azure Blob Storage ( wasbs://)
* Azure Datalake generation 1 ( adls://)
* Azure Datalake generation 2 ( abfss://)
* Delta Lake

# Jupyter | Notebooks for Experimentation
Balancing the need for experimentation and delivering. 
Data Scientists, on a pure level, should focus on modeling. However, in reality they spend 
80% of their time performing data engineering tasks. 

The majority of data scientists say that only 0 to 20% of models generated to be deployed have gotten there. 
In other words, most say that 80% or more of their projects stall before deploying an ML model. 



This initiative attempts to mitigate the
and get the data scientists up to speed.

# Machine Learning
Automate their machine learning workflows.
We formalize some common use cases in statistical learning and modeling, by providing typical workflows for use cases in Supervised Learning, Unsupervised Learning, 
Operations Research, Natural Language Processing, Computer Vision (Econometrics, Actuarial?)

* All of Supervised, Unsupervised, and Reinforcement Learning fall under the umbrella of Machine Learning, and can use Neural Networks aspects of Deep Learning. 
Therefore, Deep Learning shouldn't be a category of its own, separated from the rest.

Machine Learning: Scikit-Learn, TensorFlow, PyTorch, Keras, Caffe, H2O

| Category | Libraries|
|----------|----------|
|Supervised & Unsupervised Learning|
|Deep Learning|TensorFlow, 

We also provide functionality for automating the machine learning workflows using low-code machine learning libraries, such as PyCaret, AutoML, and Kedro.

Support for powerful frameworks and libraries such as Tensorflow, Scikit-Learn, and Pytorch

How to pick 
# Dash | Data Vizualization

# Environment Setup


Make sure you've downloaded and installed Docker and docker-compose. We will now pull the required 
images for our project, specifically Postgres, Redis, Zookeper, Kafka, Spark, Airflow

From your terminal run:

```bash




# now you can start all services:
> docker-compose -f docker-compose.yaml up -d

> docker-compose up --scale kafka=2





jupyter: on localhost:8888.
copy the password generated in the logs; access using `docker logs -f quantropy-jupyter-spark-1`
# check the condition of the containers and make sure that no containers are in unhealthy condition
> docker ps

# go into Kafka's container. NB: $(docker ps | grep docker_kafka | cut -d' ' -f1) - Will return the docker process ID of the Kafka Docker running so you can acces it
> docker exec -i -t -u root $(docker ps | grep docker_kafka | cut -d' ' -f1) /bin/bash

# create a Kafka topic
> $KAFKA_HOME/bin/kafka-topics.sh --create --partitions 4 --bootstrap-server kafka:9092 --topic test

# list Kafka topics
> $KAFKA_HOME/bin/kafka-topics.sh --bootstrap-server kafka:9092 --list

# create a Kafka consumer
> $KAFKA_HOME/bin/kafka-console-consumer.sh --from-beginning --bootstrap-server kafka:9092 --topic=test 

# open another terminal, go into the container as above, and create a Kafka producer
> $KAFKA_HOME/bin/kafka-console-producer.sh --broker-list kafka:9092 --topic=test 
```

So, what now?

1. VMs are acquired from the cloud provider.
2. The custom Docker image is downloaded from your repo.
3. Databricks creates a Docker container from the image.
4. Databricks Runtime code is copied into the Docker container.
5. The init scrips are executed. See Init script execution order.

# Requirements

## Functional Requirements:
- As an end user, I can select which broker I would like to get real-time asset prices data from. 
Brokers supported include Alpha Vantage and Alpaca Finance.
These APIs are connected to a WebSocket, which will act as our producer. This in turn will send the data 
to our message broker, Apache Kafka, the data of which will be consumed by Spark and our Non-Relational Database, MongoDB
- As an end user, I would like to observe the last 10 years worth of Yearly and Quarterly financial statements from each of the S&P 500 companies as 
of current time of writing (March 2022). Such statements are comprised of the (1) income statement, (2) cash flow statement, (3) balance sheet. 
These statements will be pulled (web crawled and scraped) from the SEC website, according to our Airflow schedule manager, who will be monitoring 
the addition of new financial reports.
- We will then perform Spark transformations on the data in MongoDB in order to 

Our ETL architecture will therefore look something like this
    
## Non-Functional Requirement: 
- Security
- Reliability
- Performance
- Maintainability
- Scalability
- Usability