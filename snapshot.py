import boto3
import datetime
import json
import requests
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# change this to whatever your table name is
table = dynamodb.Table('elasticsearch-backups')
today = datetime.date.today()

# I don't fully understand the reason for this. Following example
# http://docs.aws.amazon.com/amazondynamodb/latest/gettingstartedguide/GettingStarted.Python.04.html
pe = "#dmn, #pth, #bkt"
ean = {"#dmn": "domain", "#pth": "path", "#bkt": "bucket"}


def lambda_handler(event, context):
    nodes = table.scan(
        ProjectionExpression=pe,
        ExpressionAttributeNames=ean
        )

    for i in nodes['Items']:
        bucket = str(i['bucket'])
        path = str(i['path'])

        repository = {
            "type": "s3",
            "settings": {
                "bucket": bucket,
                "base_path": path
            }
        }
        url = i['domain'] + "/_snapshot/s3_repository"

    # create repository
        response = requests.put(
            url,
            data=json.dumps(repository)
            )
        print response.content

    # start snapshot
        url = url + "/" + str(today)
        response = requests.put(
            url
            )
        print response.content
