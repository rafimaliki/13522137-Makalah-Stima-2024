__package__ = "filereader"

import PyPDF2
from tkinter import Tk, filedialog

from algorithms.MyRegex import MyRegex

class FileReader:
    @staticmethod
    def read_pdf():
        root = Tk()
        root.withdraw() 
        file_path = filedialog.askopenfilename()
        
        text = ""
        
        file_name = file_path.split('/')[-1]
        print(f"File: {file_name}")
        
        if file_path:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    extracted_text = MyRegex.lower(page.extract_text())
                    extracted_text = extracted_text.strip()
                    extracted_text = ' '.join(extracted_text.split())
                    text += extracted_text + ' '
        
        text = text.strip()
        
        return text