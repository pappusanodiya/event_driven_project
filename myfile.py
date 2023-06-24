import boto3
mysns = boto3.client("sns")

def lw(x, y):

  mysns.publish(
    TopicArn='arn:aws:sns:us-east-1:873421059726:mylwtopic',
    Message='something is uploaded',
    Subject='I got new doc in s3 bucket',
  
  )
  print("I am Pappu Sanodiya from s3.....Calling sns....")
