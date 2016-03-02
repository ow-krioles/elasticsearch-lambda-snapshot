# elasticsearch-lambda-snapshots
-----
Uses AWS Lambda to take snapshots of Elasticsearch clusters based on records in a Dynamo table

Each entry in the Dynamo table needs to have the following three keys:

| domain                    | bucket         | path                 |
| :------------------------ | :------------- | :------------------- |
| http(s)://domain.com:port | s3-bucket-name | /path/for/snapshots/ |

When triggered, the function will loop over all entries in the table, register an S3 repository named `s3_repository` and initiate a full snapshot.
