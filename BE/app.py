import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bootcamp-votes')

def submit_vote(event, context):
  body = json.loads(event['body'])
  vote_data = {
    'date': body['vote'],
    'count': 1,  # Initial vote count for new date
  }

  # Check if date already exists in table, increment count
  existing_vote = table.get_item(Key={'date': vote_data['date']})
  if 'Item' in existing_vote:
    vote_data['count'] = existing_vote['Item']['count'] + 1
    table.update_item(
      Key={'date': vote_data['date']},
      UpdateExpression='SET count = :c',
      ExpressionAttributeValues={':c': vote_data['count']}
    )
  else:
    table.put_item(Item=vote_data)

  return {
    'statusCode': 200,
    'body': json.dumps({'message': 'Vote submitted successfully!'})
  }
