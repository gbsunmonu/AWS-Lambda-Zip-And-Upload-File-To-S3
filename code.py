import json
import boto3
s3_client=boto3.client('s3')

# lambda function to copy file from 1 s3 to another s3
def lambda_handler(event, context):
    #specify source bucket
    source_bucket_name="gb1212"
    #get object that has been uploaded
    file_name='excel_data/1665765223948_DATA (1).csv'
    #specify destination bucket
    destination_bucket_name='jaho1212'
    #specify from where file needs to be copied
    copy_object={'Bucket':source_bucket_name,'Key':file_name}
    #write copy statement 
    
    s3_client.copy_object(CopySource=copy_object,Bucket=destination_bucket_name,Key="file_name.zip")

    return {
        'statusCode': 3000,
        'body': json.dumps('File has been Successfully Copied')
    }