from document_analysis.table_extractor import PDFExtractor
import document_analysis.utils as utils

import os
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser(description='Analyze the PDF documents in the S3 bucket and store the responses')
    
    parser.add_argument("bucket_name", help="bucket name",
                        type=str)
    parser.add_argument("--path", help="folder prefix in the bucket",
                        default="", type=str)
    parser.add_argument("--output_folder", help="output folder path to store the responses",
                        default="output", type=str)
    parser.add_argument("--file_type", help="file type",
                        default="pdf", type=str)
    
    args = parser.parse_args()
    return args

def analyze_documents(bucket_name, path, output_folder, file_type):       
    documents = utils.get_file_names_s3(bucket_name, path, file_type)
    
    if len(documents) > 0:
        print('Running document analysis on {} {} documents:'.format(len(documents), file_type[0]))
        for index, file_path in enumerate(documents):
            file_name, _ = utils.get_file_name_and_extension(file_path)

            extractor = PDFExtractor(bucket_name, file_path)
            print("Started analysis on document #{}".format(index+1))
            response = extractor.extract_async()

            output_path = os.path.join(output_folder,file_name)
            os.makedirs(output_path, exist_ok = True)
            utils.write_file(os.path.join(output_path,"response.json"), json.dumps(response))
        print("Analysis completed on {} documents.".format(len(documents)))
        print("Output folder is {}".format(output_folder))
    else:
        print('No {} document found'.format(file_type[0]))

if __name__ == '__main__':
    args = parse_args()
    bucket_name = args.bucket_name
    path = args.path
    output_folder = args.output_folder
    file_type = [args.file_type]
    analyze_documents(bucket_name, path, output_folder, file_type)
    