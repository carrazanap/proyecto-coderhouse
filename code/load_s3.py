#!/usr/bin/env python3

import boto3
import pathlib
import os

AWS_REGION = "us-east-2"
#Cargo los datos de la conexion con mi cuenta de AWS
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

client = boto3.client("s3", region_name=AWS_REGION, 
aws_access_key_id=AWS_ACCESS_KEY,
aws_secret_access_key=AWS_SECRET_KEY)

print("CREANDO BUCKET...")

bucket_name = "bucket-coder-carrazana"

location = {'LocationConstraint': AWS_REGION}

response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")

print("Uploading File ...")

#Funcion que carga el csv al bucket
def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{bucket_name}'")

upload_files(f"./data/Happiness_final.csv", bucket_name, 'Happiness_final.csv')