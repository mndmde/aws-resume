import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-test')

def lambda_handler(event, context):
    response = table.get_item(Key={
        'Id':'0'
    })
    views = response['Item']['views']
    views = views + 1
    print(views)
    response = table.put_item(Item={
        'Id':'0',
        'views': views
    })
    
    return views