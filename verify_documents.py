import document_analysis.utils as utils

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Verify the PDF documents in the S3 bucket before analyzing')
    
    parser.add_argument("bucket_name", help="bucket name",
                        type=str)
    parser.add_argument("--path", help="folder prefix in the bucket",
                        default="", type=str)
    parser.add_argument("--file_type", help="file type",
                        default="pdf", type=str)
    
    args = parser.parse_args()
    return args

def verify_documents(bucket_name, path, file_type):
    documents = utils.get_file_names_s3(bucket_name, path, file_type)
    if len(documents) > 0:
        print("Detected {} {} documents:".format(len(documents), file_type[0]))
        for index, file_path in enumerate(documents):
            print("\t {} - {}".format(index+1, file_path)) 
    else:
        print("No {} document found".format(file_type[0]))

if __name__ == '__main__':
    args = parse_args()
    bucket_name = args.bucket_name
    path = args.path
    file_type = [args.file_type]
    verify_documents(bucket_name, path, file_type)
    