# elasticsearch-lambda-snapshots

es-snapshot is an AWS Lambda function for use with Lambder.

Uses AWS Lambda to take snapshots of Elasticsearch clusters based on records in a Dynamo table

Each entry in the Dynamo table needs to have the following three keys:

| domain                    | bucket         | path                 |
| :------------------------ | :------------- | :------------------- |
| http(s)://domain.com:port | s3-bucket-name | /path/for/snapshots/ |

When triggered, the function will loop over all entries in the table, register an S3 repository named `s3_repository` and initiate a full snapshot.

## Getting Started

1.  Test the lambda function
        python lambda/es-snapshot/es-snapshot.py
2.  create zip
        ./build.sh
3.  Create Lambda function using zip file.

## Notes
1. The iam and input dirs, as well as lambder.json are for use by Lambder. You can use Lambder for testing, but it is not part of our workflow at this time.
2. The Dockerfile is included only for testing purposes.
