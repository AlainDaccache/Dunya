# Overview
Raison d’être: Let's be real. You can count on your fingers the people who enjoy setting up their development environments; 
whether it's the daunting bash scripts, `$HOME` environment variables, dependencies circular hell; this project thereby aims at minimizing the hassle of setting up projects while putting on display 
the commonly used data tools and processes in today's industry. 
* **Modern Data Stack:**. We understand there is no one-size-fits-all solution, that tools come and go but the underlying 
principles remain. This project attemps to be agnostic to the specific components i.e. cloud providers, data warehouses, 
message brokers / queues, caches etc. for a 'plug-and-play' kind of experience.
* **Low-code / No-code:** While I don't particularly advocate for this movement partly due to the genericity vs. specificity tradeoff, 
we can still abstract away a stack of tools and processes that can  be used in a variety of data-oriented initiatives.
* **Clear Responsibilities:** With the constant refinement of this emerging industry, we are still ambiguously defining and refining the roles
that would make up a data-oriented team. This project does not only provide with tools, but also technical + business processes in order to align teams specifically for
data-oriented initiatives.

## On the Shoulder of Giants: Layers of Abstraction

This is what I aim to provide in this repository
* **Layer 1 | Infra as a Service:** This is the foundation that our service is built upon i.e. an IaaS (i.e. local or cloud storage, compute, network), so we're not technically IaaS.
* **Layer 2 | Platform/Data as a Service:** We extend IaaS to provide ready-made data mechanisms for common use cases that we can provide to clients to build their models on. 
Mutual agreement (i.e. on the API level), that a client can use for its Business Intelligence reporting purposes.
* **Layer 3 | Software/Model as a Service:** We provide clients with either (1) pre-trained models, or (2) meta-models 
(i.e. through pickled files or APIs), from which they'll plug in their data for 

With these layers, we allow for different architectures based on your use-cases, and combinations thereof.
* **Formats of Data:** Structured, Semi-Structured, Unstructured.
* **Storage of Data:** Databases (SQL+NoSQL-based), Data Warehouses and Data Lakes.
* **Sequencing of Data:** ETL and ELT pipelines.
* **Processing of Data:** OLAP and OLTP.
* **Periodicity of Data:** Stream and Batch processing.
* **Types of Data:** Continuous, Discrete

Finally, we aim at visibility across the dimensions that make up **data quality** through periodic automated reporting for accuracy, 
completeness, consistency, validity, uniqueness, and timeliness.

## Overview of a Data Initiative

### Extracting Data

* **File Transfer Protocols:** HTTP(S), FTP(S), (S)FTP.
* **Application Programming Interfaces:** RESTful API, \[G]RPC, GraphQL. Get acquainted with the Limits and Quotas on API Requests.
You can get started on *SaaS* based APIs (i.e. Salesforce), *Social Media* (Twitter, Reddit, Facebook), and *Governmental Websites* (i.e. StatsCan).
* **Web Crawling & Scraping:** Think Selenium for crawling, BeautifulSoup for scraping and parsing... Ensure you read the `robots.txt` file of a website you want to extract information from, to evaluate whether you're 
permitted to scrape data. The rate at which you can call isn't very visible until they block your IP from making 
requests for some time. You can always try strategies like `sleep`ing or rotating proxies and changing IP address to by-pass the limits. 
Use at your own risk of having your IP address blocked. We provide an example of crawling/scraping the *SEC* website

Newcomer data integration solutions (such as **FiveTran** and **Stitch**) attempt to abstract away the complexity of
(1) communicating with APIs of such SaaS, (2) making transformations (i.e. Spark w/ Databricks, SQL w/ dbt...), 
as well as (3) maintaining such pipelines (in case of provider updates or edge cases).

### Loading / Storing Data

### Processing / Transforming Data

Airflow should support Pandas, Dask, Spark, and SQL-based Queries.


The end result (i.e. in a DB/DW) can now either be
* Exposed by an API for development purposes.
* Exported to BI tools for analysis purposes.

# The Solution

Our architecture supports the data patterns mentioned above.

## Microservices Architecture

Standardizing: We present three zones, each for a specific purpose
* **Raw:**
* **Curated:**
* **Consumption:**

Our images come built-in with connectors to common data sources:
* **Databases:** Postgres (``)
* **Data Warehousing:** Redshift, Snowflake, BigQuery.
* **Data Lakes:** Delta Lake, AWS S3 (`s3a://`), Google Cloud Storage (`gs://`), Azure Blob Storage (`wasbs://`), 

We also provide support for using the
* **Cloud Providers:** AWS (Amazon), Azure (Microsoft), GCP (Google).




* Asynchronous /_ Message Brokers / Caches: WebSocket, Memcached vs. Redis, Kafka vs. RabbitMQ



### Architecture Components - Specs

Finally, they contain a combination of versions from the components listed below. 
You can play around with the versions depending on your needs, Feel free to specify them in the `.env` file.
However, you should note that not all combinations would be compatible, and our default versions is the currently stable.
If at any point, you believe you messed up with versioning and need to roll-back, use the `docker-compose down --volumes --rmi all` command, then re-run your original commands.

| Service    | Function | Image | Versions Available| Env Variabe | Host/Port      |
|------------|----------|-------|--------------------|------------|----------------|
| PostgreSQL | RDBMS    |       |                    |            | [localhost:5432](localhost:5432) |
| Spark      |          |       |                    |            | [localhost:8181](localhost:8181)|
| Airflow    | Data Workload Scheduler & Orchestrator|  |  |          | [localhost:8080](localhost:8080)|
| Sphinx     | Documentation Generator|
| DataDog    | Monitoring / Observability |
| Redis      |          |       |                    |            | [localhost:6379](localhost:6379)|

## Environment Setup

* running on a Debian inside WSL2, you'll get a `/usr/bin/env: ‘bash\r’: No such file or directory` error due to the 
carriage returns on Windows; therefore, use `git config --global core.autocrlf false` before cloning.
* First, download and install [Git](https://git-scm.com/downloads), and clone the [Dunya project](https://github.com/AlainDaccache/Dunya.git)
* Have your Python environment ready (as well `pip install -r requirements.txt` file) if you wish to develop locally.
* Have an [AWS Account](https://aws.amazon.com/) ready, and install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
* Download [Docker Desktop](https://www.docker.com/products/docker-desktop/) with at least 4GB of RAM, and [Docker Compose](https://docs.docker.com/compose/install/) v1.27.0 or later.
* Then, create an `.env` file at the root (`cd Dunya`) and fill in your credentials for the APIs, DBs, and other tools you'd like to use. If you leave empty, we won't set it up.

```.env
# Postgres DB Credentials
POSTGRES_VERSION=9.6
POSTGRES_NAME=postgres
POSTGRES_DB=airflow
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow

# Twitter API Credentials
TWITTER_CONSUMER_KEY=<your_twitter_consumer_key>
TWITTER_CONSUMER_SECRET=<your_twitter_consumer_secret>
TWITTER_USER_KEY=<your_twitter_user_key>
TWITTER_USER_SECRET=<your_twitter_user_secret>

# Airflow Config
AIRFLOW_VERSION=2.2.4
AIRFLOW_IMAGE_NAME=dunya-airflow:2.2.4
AIRFLOW_UID=50000

# Spark Config
SPARK_IMAGE_NAME=dunya-spark:latest
SPARK_VERSION="3.1.2"
HADOOP_VERSION="3.2"

# Sphinx Config
SPHINX__PROJECT_NAME=Dunya
SPHINX__AUTHOR_NAME=Alain
SPHINX__PROJECT_RELEASE=0.1
SPHINX__PROJECT_LANGUAGE=en
```

AWS:
`cat ~/.aws/config`
`cat ~/.aws/credentials`
Go to your Bash i.e. `"C:\Program Files\Git\bin\sh.exe" --login`.
* Then, run the Bash script `/bin/sh setup_infra.sh` to see the arguments you'll need to pass
 
 If you see a `-bash: '\r': command not found` error, try `dos2unix <file_name>` in order to modify Windows 
 newline characters (CR LF) so they are Unix / Cygwin compatible (LF).
 
 Your bucket should contain:
- The PySpark script
- The input dataset
- Your output results folder
- Your log files folder

### Bootstrapping our Services

We provide a `setup_infra.sh` file from which you can run everything in this section; however this write-up aims 
at giving you a clearer idea of the services underneath and their usage, in a tutorial form.

## Package Dependency & Environment Management
This environment comes with pip and conda so that it's easy to to install additional Python packages.

|Manager|Is Package Manager?|Is Environment Manager?|
|-------|-------------------|-----------------------|
|pip    |      Yes          |         No            |
|PyEnv  |      No           |        Yes            |
|Pipenv|
|Poetry|
|Virtualenv (venv) and Pipenv
| Conda / Anaconda | Yes (Secondarily) |Yes (Primarily)|


Dependency Management
* Back-compatibility
* 

## Sphinx | Documentation Generator

```

```

## Airflow | Data Worfklow Scheduler & Orchestrator

First, we initialize Airflow's database; we need to run database migrations and create the first user account for Airflow.
```
> docker-compose up airflow-init
```
You should see
```
airflow-init_1       | User "airflow" created with role "Admin"
airflow-init_1       | 2.2.4
```

We extend Puckel's Airflow image capabilities with our own for JDK-8 and Spark support, and we build the new image

**WARNING:** For jdk-8 | `--no-check-certificate` to download Spark's binary (in `airflow/Dockerfile`) because of certificate `archive.apache.org` is from 
an unknown issuer; so adding this flag makes us susceptible to Man-in-the-middle attack. Use at your own risk; trying to 
find a workaround meanwhile, and any help is immensely appreciated!

```commandline
docker build ./airflow --tag dunya-airflow:2.2.0
```

We then set this image in `docker-compose.yaml` file, using its tag:

```
echo "AIRFLOW_IMAGE_NAME=dunya-airflow:2.2.0" >> .env
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

## Django / Nginx / Gunicorn | Backend App

you can run the `web` service to create a Django project
```
# The following command instructs compose to run django-admin startproject composeexample in a container, 
# using the web service’s image and configuration. 
> docker-compose run web django-admin startproject app .
```

* Dev and test environments
* Gunicorn and Nginx for Production environment

## React | Frontend App

## Postgres | RDBMS

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

## MongoDB | NoSQL Database

## Kafka | Message Broker

## Spark | Large-Scale Data Processor

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

You can run a Spark Job via Airflow:
```
docker exec -it dunya_airflow-webserver_1 spark-submit --master spark://spark-master:7077 /usr/local/spark/app/hello-world.py /usr/local/spark/resources/data/movies.csv
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
docker exec -d airflow-webserver_1 airflow connections add 'redshift' --conn-type 'Postgres' --conn-login $REDSHIFT_USER --conn-password $REDSHIFT_PASSWORD --conn-host $REDSHIFT_HOST --conn-port $REDSHIFT_PORT --conn-schema 'dev'
```

### Running Spark jobs in Jupyter

### Processing data stored in Data Warehouses
* Snowflake

### Processing data stored in Data Lakes

# Data Science

There is a trend in ML Engineering branching out of Data Science. While Data Science is becoming more analysis-based, 
its counterpart is becoming more product-based. Data Science thus focuses more on tasks such as
1. creating metrics, 
2. designing experiments, and 
3. performing ad-hoc analyses (i.e. cohort analysis, customer segmentation, etc.)

## Data Science Process

* Type of Data: Tabular, Text, Images
* Categorical, Continuous...
* Classification, Regression
* 

Standardizing the process: Based on your use case, you'll need to make some decisions regarding the requirements
* Gathering the data: Our data will therefore be loaded in the appropriate storage type (DB, WH) and data format.
    - Building data pipelines to cover both ETL/ELT paradigms. 
    - Cover both real-time/batch processing, as well as OLAP/OLTP. You decide if the data will need to be fed continuously.
    - Supports different formats of data, from 
        - unstructured (text, image, audio, video) which will cover the NLP and CV portions of AI.
        - semi-structured (JSON, XML...) which could cover both NLP/CV and more ML cases
        - structured
        

Pre-Processing: the data still might not be in the desired format:
* Talk about Data Quality

### Exploratory Data Analysis: 

Talk about data profiling
* Analysis Packages: NumPy, SciPy, Pandas, Statsmodels
* Visualization Packages: matplotlib, seaborn

You will typically be evaluating the features themselves, as well as the interactions between them:
* For the feature itself; evaluate distribution with tools such as `pandas-profiling`
* Running hypothesis tests; where you'll decide on the appropriate test to run based on the variable types (continuous, discrete), assumptions (normality), and groups
* Evaluate other interactions between features; such as correlation, feature importance (typically `RandomForest`)
* Selecting features; using the previous point, as well as doing some feature engineering to reduce dimensionality (PCA).

### Feature Engineering

Overlap with DS and MLE.

### Jupyter | Notebooks for Experimentation
Balancing the need for experimentation and delivering. 
Data Scientists, on a pure level, should focus on modeling. However, in reality they spend 
80% of their time performing data engineering tasks. 

The majority of data scientists say that only 0 to 20% of models generated to be deployed have gotten there. 
In other words, most say that 80% or more of their projects stall before deploying an ML model. 

This initiative attempts to mitigate this problem and get the data scientists up to speed.

### Dash | Data Vizualization

# Machine Learning Engineering
Project Structure: cookie-cutter for Data Science

* **Artifacts:** Contains your data processors, and models in (`.pkl`, `.joblib`)

## Infrastructure Setup / IaaS | Terraform, Puppet, Chef, Ansible

### Logging

## API Development | Django REST, Flask, FastAPI

## Machine Learning Workflow Automation
We formalize some common use cases in statistical learning and modeling, by providing typical workflows for use cases in Supervised Learning, Unsupervised Learning, 
Operations Research, Natural Language Processing, Computer Vision (Econometrics, Actuarial?)

* All of Supervised, Unsupervised, and Reinforcement Learning fall under the umbrella of Machine Learning, and can use Neural Networks aspects of Deep Learning. 
Therefore, Deep Learning shouldn't be a category of its own, separated from the rest.

Support for powerful, deployment-ready ML/DL frameworks and libraries, cited below:

| Category | Libraries|
|----------|----------|
|Supervised & Unsupervised Learning| Scikit-Learn
|Deep Learning|TensorFlow, PyTorch, Keras, Caffe|

Include H2O.

### PyCaret & AutoML | Low-Code Machine Learning

We also provide functionality for automating the machine learning workflows using low-code machine learning libraries, such as PyCaret, AutoML, and Kedro.

###

We recalibrate our models on 
* Fixed/Schedule: Daily, Weekly, etc.
* Event/Dynamically: based on some event which changed the data's properties

We will simulate in two ways:
* Cron-based sending messages from a table i.e. Kafka
* Locust

Airflow will then trigger our API, which will
(1) Give the prediction for the real-time case. Also supports batch-predictions.
(2) Store the data (X) plus our prediction (y) in the database
(3) Periodically fetches the actual value (Y) and compares to (y)
(4) Dynamically re-balance the load between our models based on the differentials
(5) Run drift-analysis for model drift (concept drift + data drift)

### Locust | Load Testing Tool to Simulate User Behaviour


## Monitoring Model Performance

* Software Engineering Perspective: Latency, Throughput, Requests...
* Machine Learning: Model Drift
* 
### Model Explainability / Explainable AI
Interpretable Machine Learning Models. Tools
* ELI5
* LIME
* SHAP
* Yellowbrick
* Alibi
* Lucid

### MLFlow | Experiments Monitoring

### Promotheus | Performance Metrics Monitoring & Storage

### Grafana | Performance Metrics Visualization

# References
* https://github.com/jeremyjordan/ml-monitoring
* https://www.analyticsvidhya.com/blog/2020/03/6-python-libraries-interpret-machine-learning-models/
* https://medium.com/codex/executing-spark-jobs-with-apache-airflow-3596717bbbe3
* https://docs.python.org/3/library/http.client.html
* https://docs.python.org/3/library/ftplib.html
* https://github.com/puckel/docker-airflow/blob/master/docker-compose-CeleryExecutor.yml
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

# Draft:
* Docker: enables system administrators and developers to build distributed applications.
* This environment comes with Python 3.6 & PySpark support built on JDK 8

Make sure you've downloaded and installed Docker and docker-compose. We will now pull the required 
images for our project, specifically Postgres, Redis, Zookeper, Kafka, Spark, Airflow

From your terminal run:

```bash

# now you can start all services:
> docker-compose -f docker-compose-jdk-8.yaml up -d
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

Use Cases Covered: https://h2o.ai/solutions/use-case/
