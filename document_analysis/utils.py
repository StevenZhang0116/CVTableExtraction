import boto3
import os
import csv

def get_file_names_s3(bucket_name, prefix, allowed_file_types=["pdf"]):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    files = []

    for obj in bucket.objects.filter(Prefix=prefix):
        file = obj.key
        _, ext = get_file_name_and_extension(file)
        if(ext.lower() in allowed_file_types):
            files.append(file)

    return files

def get_file_name_and_extension(file_path):
    basename = os.path.basename(file_path)
    dn, dext = os.path.splitext(basename)
    
    return (dn, dext[1:])

def read_file(file_name):
    with open(file_name, 'r') as document:
        return document.read()

def write_file(file_name, content):
    with open(file_name, 'w') as document:
        document.write(content)