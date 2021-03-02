import boto3
import time

class PDFExtractor:
    def __init__(self, bucket_name, file_path, client=None):
        self.bucket_name = bucket_name
        self.file_path = file_path
        self.client = boto3.client('textract') if client is None else client
        
    def start_job(self):
        response = self.client.start_document_analysis(
            DocumentLocation={
                'S3Object': {
                    'Bucket': self.bucket_name,
                    'Name': self.file_path
                }
            },
            FeatureTypes=['TABLES']
        )
        
        return response["JobId"]

    def is_job_complete(self, job_id):
        response = self.client.get_document_analysis(JobId=job_id)
        status = response["JobStatus"]
        print("Job status: {}".format(status))

        while(status == "IN_PROGRESS"):
            time.sleep(5)
            response = self.client.get_document_analysis(JobId=job_id)
            status = response["JobStatus"]
            
        print("Job status: {}".format(status))

        return status
    
    def get_job_results(self, job_id):
        pages = []
        response = self.client.get_document_analysis(JobId=job_id)
        pages.append(response)
        nextToken = None
        
        if('NextToken' in response):
            nextToken = response['NextToken']

        while(nextToken):
            response = self.client.get_document_analysis(JobId=job_id, NextToken=nextToken)
            pages.append(response)
            nextToken = None
            if('NextToken' in response):
                nextToken = response['NextToken']
                
        return pages

    def extract_async(self):
        job_id = self.start_job()
        print("Started async job with id: {}".format(job_id))
        status = self.is_job_complete(job_id)
        
        if(status == "SUCCEEDED"):
            response = self.get_job_results(job_id)
            return response