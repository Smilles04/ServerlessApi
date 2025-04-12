import boto3
dynamodb_client = boto3.client('dynamodb')

def main(event, context):
  dynamodb_client.put_item(TableName='WeatherData', Item={'id': {'S': '1'}, 'Weather': {'S': 'Sunny'}})
  return {
      'statusCode': 200,
      'body': 'Successfully inserted data!'
  }