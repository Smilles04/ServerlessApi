import boto3
from boto3.dynamodb.types import TypeDeserializer
dynamodb_client = boto3.client('dynamodb')

def main(event, context):
  items = dynamodb_client.scan(TableName='WeatherData')["Items"]
  result = [unmarshal_dynamodb_item(item) for item in items]

  return {
      'statusCode': 200,
      'body': str(result)
  }

def unmarshal_dynamodb_item(item):
    deserializer = TypeDeserializer()
    return {k: deserializer.deserialize(v) for k, v in item.items()}