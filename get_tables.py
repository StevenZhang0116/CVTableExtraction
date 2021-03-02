from document_analysis.output_generator import OutputGenerator
import document_analysis.utils as utils

import os
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser(description='Get tables from document analysis responses and save them in csv format')
    
    parser.add_argument("path", help="folder containing all document analysis responses returned from running analyze_documents.py",
                        type=str)
    
    args = parser.parse_args()
    return args

def get_tables(path):   
    found = False
    for root, directories, files in os.walk(path): 
        for file_name in files:  
            if file_name == "response.json":
                response_path = os.path.join(root, file_name)
                response = json.loads(utils.read_file(response_path))
                output = OutputGenerator(response)
                found = True

                csv_list = output.to_csv()
                print("Found document analysis response in {} and retrieved {} tables".format(root, len(csv_list)))
                for i in range(len(csv_list)):
                    csv = csv_list[i]
                    utils.write_file(os.path.join(root, "table_{}.csv".format(i+1)), csv)
    if not found:
        print("No document analysis response found")

if __name__ == '__main__':
    args = parse_args()
    path = args.path
    get_tables(path)
    