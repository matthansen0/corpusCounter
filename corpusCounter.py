## Matt Hansen 
## https://github.com/matthansen0

import os
import pandas as pd
from PyPDF2 import PdfReader

def count_words_in_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        total_words = 0
        if reader.is_encrypted:
            raise ValueError("File is encrypted")
        for page in reader.pages:
            text = page.extract_text()
            total_words += len(text.split())
        return total_words
    except Exception as e:
        print(f"Skipped file {file_path} due to error: {str(e)}")
        return 0

def count_words_in_csv(file_path):
    df = pd.read_csv(file_path)
    text = " ".join(df.values.flatten().astype(str))
    total_words = len(text.split())
    return total_words

directory = r'C:\files\path'  # your directory path

total_word_count = 0
file_count = 0
skipped_files = []
for dirpath, dirs, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(dirpath, filename)
        if filename.endswith('.pdf'):
            print(f"Processing PDF {filepath}")
            words = count_words_in_pdf(filepath)
            if words == 0:  # if the file was skipped
                skipped_files.append(filepath)  # add it to the list of skipped files
            total_word_count += words
        elif filename.endswith('.csv'):
            print(f"Processing CSV {filepath}")
            total_word_count += count_words_in_csv(filepath)
        file_count += 1
        if file_count % 10 == 0:
            print(f"Processed {file_count} files so far with total word count: {total_word_count}")

print(f'Total word count: {total_word_count}')

# print out the skipped files
if skipped_files:
    print("\nThe following files were skipped due to errors:")
    for file in skipped_files:
        print(file)
