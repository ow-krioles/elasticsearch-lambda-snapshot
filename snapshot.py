import boto3
import datetime
import json
import requests
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('elasticsearch-backups')
today = datetime.date.today()

pe = "#dmn, #pth, #bkt"
ean = {"#dmn": "domain", "#pth": "path", "#bkt": "bucket"}

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
    print repository
    url = i['domain'] + "/_snapshot/s3_repository"
    response = requests.put(
        url,
        data=json.dumps(repository)
        )
    print response.content
    url = url + "/" + str(today)
    response = requests.put(
        url
        )
    print response.content
