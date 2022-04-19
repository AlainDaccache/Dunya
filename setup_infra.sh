#!/bin/bash

# Load environment variables from dotenv / .env file in Bash
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi

# Validate Docker is running
if ! docker info >/dev/null 2>&1; then
    echo "Docker does not seem to be running, run it first and retry"
    exit 1
fi

# Configuring AWS Credentials & Region
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set default.region $AWS_DEFAULT_REGION

echo "Your .aws/config file looks like this:"
cat ~/.aws/config

echo "Your .aws/credentials file looks like this:"
cat ~/.aws/credentials

AWS_ID=$(aws sts get-caller-identity --query Account --output text | cat)

# Creating Bucket

echo "Creating bucket "$1""
aws s3api create-bucket --acl public-read-write --bucket $1 --output text >> setup.log

echo "Clean up stale local data"
rm -f data.zip
rm -rf data
echo "Download data"
aws s3 cp s3://start-data-engg/data.zip ./
unzip data.zip


#--------------------------------------------------------------------------
#                                   Airflow
#--------------------------------------------------------------------------
echo "Spinning up local Airflow infrastructure"
rm -rf logs
mkdir logs
rm -rf temp
mkdir temp

# Airflow
# Now built in docker-compose: docker build ./airflow --tag "$AIRFLOW_IMAGE_NAME"
docker-compose up airflow-init
docker-compose up -d
echo "Sleeping 5 Minutes to let Airflow containers reach a healthy state"
sleep 300

#echo "Creating an AWS EMR Cluster named "$SERVICE_NAME""
#aws emr create-default-roles >> setup.log
#aws emr create-cluster --applications Name=Hadoop Name=Spark \
#--release-label emr-6.2.0 --name $SERVICE_NAME \
#--scale-down-behavior TERMINATE_AT_TASK_COMPLETION  \
#--service-role EMR_DefaultRole \
#--instance-groups

docker exec spark-master spark-submit \
--master spark://spark-master:7077 \
/usr/local/spark/app/health_violations.py \
--data_source /usr/local/spark/resources/data/Food_Establishment_Inspection_Data.csv \
--output_uri /usr/local/spark/resources/data/output.csv
