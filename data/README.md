# Downloading Files from S3

This is a simple script to download files from an S3 bucket. Make sure you have these enviroment variables set:

1. BUCKET_NAME: name of the bucket where you stored your files

2. KEYS: name of the files you want to download, for multiple files use ; as a separtor

3. OUT_DIR: where to store these files in the local path

4. ACCESS_KEY: the access key for your AWS account or an account that has access to the bucket (safer)

5. SECRET_KEY: the secret key for your AWS account or an account that has access to the bucket (safer)
