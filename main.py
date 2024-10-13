import os
import time
from concurrent.futures import ProcessPoolExecutor
from pdf_processor import PDFProcessor
from mongo_handler import MongoHandler
from summarizer import Summarizer
from keyword_extractor import KeywordExtractor

def process_pdf(pdf_file):
    try:
        text = pdf_processor.extract_text(pdf_file)
        summary = summarizer.summarize(text)
        keywords = keyword_extractor.extract_keywords(text)

        mongo_handler.update_document(pdf_file, summary, keywords)
        print(f"Processed {pdf_file}")
    except Exception as e:
        print(f"Error processing {pdf_file}: {e}")

if __name__ == "__main__":
    folder_path = "D:\\AiInternTask\\downloaded_pdfs" 
    mongo_uri = 'mongodb://localhost:27017/'  # MongoDB URI
    db_name = 'pdf_database'

    mongo_handler = MongoHandler(mongo_uri, db_name)
    pdf_processor = PDFProcessor(folder_path)
    summarizer = Summarizer()
    keyword_extractor = KeywordExtractor()

    # For ingesting PDFs and storing metadata in MongoDB
    pdf_files = pdf_processor.ingest_pdfs()
    for pdf_file in pdf_files:
        document = {
            'document_name': pdf_file,
            'path': os.path.join(folder_path, pdf_file),
            'size': os.path.getsize(os.path.join(folder_path, pdf_file)),
        }
        mongo_handler.insert_document(document)

    # To process pdfs concurrently
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        executor.map(process_pdf, pdf_files)
    end_time = time.time()

    print(f"Processed {len(pdf_files)} PDFs in {end_time - start_time:.2f} seconds.")
