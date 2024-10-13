import os
import requests
import json

# To load the JSON file with URLs
json_file = "C:\\Users\\panka\\Downloads\\Dataset.json"  
with open(json_file, 'r') as file:
    data = json.load(file)

# For creating a directory to save the PDFs
save_folder = 'downloaded_pdfs'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Function to download PDFs
def download_pdf(pdf_url, file_name):
    try:
        response = requests.get(pdf_url)
        if response.status_code == 200:
            pdf_path = os.path.join(save_folder, file_name)
            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download {file_name}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {file_name}: {e}")

# Download all PDFs from the JSON data
for pdf_key, pdf_url in data.items():
    # To set the file name as the key with a .pdf extension
    file_name = f"{pdf_key}.pdf"
    download_pdf(pdf_url, file_name)

print("All PDFs downloaded.")
