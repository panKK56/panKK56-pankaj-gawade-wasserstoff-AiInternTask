import os
import PyPDF2

class PDFProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def ingest_pdfs(self):
        pdf_files = [f for f in os.listdir(self.folder_path) if f.endswith('.pdf')]
        return pdf_files

    def extract_text(self, pdf_file):
        with open(os.path.join(self.folder_path, pdf_file), 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + '\n'
            return text.strip()
