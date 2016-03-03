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
    print "started"

    print "scanning table"
    nodes = table.scan(
        ProjectionExpression=pe,
        ExpressionAttributeNames=ean
        )

    print "nodes are " + str(nodes)

    for i in nodes['Items']:
        bucket = str(i['bucket'])
        path = str(i['path'])

        print "bucket is " + str(i['bucket'])
        print "base_path is " + str(i['path'])

        print "setting repository json"
        repository = {
            "type": "s3",
            "settings": {
                "bucket": bucket,
                "base_path": path
            }
        }
        print "repository json is " + json.dumps(repository)

        print "setting url path"
        url = i['domain'] + "/_snapshot/lambda_s3_repository"
        print "url path is " + url

    # create repository
        print "creating repository"
        response = requests.put(
            url,
            data=json.dumps(repository)
            )
        print response.content

    # start snapshot
        print "starting snapshot"
        url = url + "/" + str(today)
        response = requests.put(
            url
            )
        print response.content

lambda_handler("test", "test")
