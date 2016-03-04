# elasticsearch-lambda-snapshots

es-snapshot is an AWS Lambda function for use with Lambder.

Uses AWS Lambda to take snapshots of Elasticsearch clusters based on records in a Dynamo table

Each entry in the Dynamo table needs to have the following three keys:

| domain                    | bucket         | path                 |
| :------------------------ | :------------- | :------------------- |
| http(s)://domain.com:port | s3-bucket-name | /path/for/snapshots/ |

When triggered, the function will loop over all entries in the table, register an S3 repository named `s3_repository` and initiate a full snapshot.

REQUIRES:
* python-lambder

## Getting Started

1) Test the lambda function

    python lambda/es-snapshot/es-snapshot.py

2) Deploy the sample Lambda function to AWS

    lambder functions deploy

3) Invoke the sample Lambda function in AWS

    lambder functions invoke

4) Add useful code to lambda/es-snapshot/es-snapshot.py

5) Add any permissions you need to access other AWS resources to iam/policy.json

6) Update your lambda and permissions policy in one go

    lambder functions deploy
