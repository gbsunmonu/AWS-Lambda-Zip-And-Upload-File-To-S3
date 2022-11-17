# AWS-Lambda-Zip-And-Upload-File-To-S3

In other to solve the problem 

I attacked it by first suggested solution manually following the steps below

- I created S3 bucket and I created a folder inside the S3 bucket named excel_data which stand as the source 

-I created another S3 bucket and created a folder inside the S3 bucket called destination 

- I uploaded excel and csv file in my source folder 
- I downloaded the file I uploaded in my source folder, and I compressed it 
-The compressed data was later uploaded to destination folder that I created.

### Automating my process using Lambda

- Created Lambda function manually

- Added policy to Get object from s3 source folder and policy to put object in my destination folder
- Set trigger using event Bridge to run lambda function every one hour 
- Get csv files from s3 bucket, source folder 
-Put it in S3 bucket, destination folder and zip the file 


Room for improvement 
- use Terraform to create aws resources 
- have lambda code bringing down n sorting through source s3 bucket to pick files that need to be move to destination bucket
