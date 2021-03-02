from document_analysis.trp import Document
import json

class OutputGenerator:
    def __init__(self, response):
        self.response = response
        
    def to_csv(self):
        document =  Document(self.response)
        results=[]
        index=0
        
        for page in document.pages:
            for table in page.tables:
                csv=''
                for r, row in enumerate(table.rows):
                    for c, cell in enumerate(row.cells):
                        csv += '{}'.format(cell.text) + ","
                    csv += '\n'
                    
                results.append(csv)
                index+=1
                
        return results