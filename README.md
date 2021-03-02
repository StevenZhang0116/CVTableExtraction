# CVTableExtraction

Continuing work of [this](https://github.com/StevenZhang0116/ScienceDirectWebCrawler) project. Automatically extract tables from PDF documents stored in an S3 bucket using Amazon Textract ([AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)). Through this computer vision approach, people could effectively gather information in patches and do some relevant analysis. The whole procedure is separated into verifying documents, analyzing documents, and getting tables (saving in CSV format). 

## Example of implementations

```
python3 verify_documents.py "my-bucket" --path="files/documents"
python3 analyze_documents.py "my-bucket" --path="files/documents" --output_folder="documents/tables"
python3 get_tables.py --path="documents/tables"
```
