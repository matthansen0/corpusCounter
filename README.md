# Corpus Counter

When looking to feed documents into an embedding AI model, you may want to know how much it's going to cost. Azure OpenAI and OpenAI both charge by tokens, and they are both roughly .75-1 token per word of text. 

How though, do I know how many words are in a corpus of documents? That is the reason why I create this script, it is used to calculate the total number of words in all PDF and CSV files in a specified directory and its subdirectories.

## To-Do List

- [ ] Add support for .doc and .docx
- [ ] Add .txt support
- [ ] Add .eml support

## What It Does

The script performs the following steps:

1. Iterates over each file in the specified directory and its subdirectories.
    - If the file is a PDF:
        - It uses PyPDF2 to extract the text and count the words.
    - If the file is a CSV:
        - It uses pandas to read the file into a DataFrame.
        - It then concatenates all values into a single string and counts the words.
    - It keeps a running total of the word count.

2. Handles unreadable files:
    - If the script encounters an unreadable file (for example, a PDF that is encrypted), it prints an error message and skips the file.

3. Provides progress updates:
    - Every 10 files, it prints a progress update showing how many files it has processed and the total word count so far.

4. Prints the final result:
    - At the end, it prints out the total word count across all files.

5. Prints a list of skipped files:
    - It also prints out a list of all files that were skipped due to errors.


## Prerequisites

Before running this script, make sure you have Python installed and the following packages:

- pandas: `pip install pandas`
- PyPDF2: `pip install PyPDF2`

Also, replace `'your-directory-path'` in the script with the directory containing your PDFs and CSVs.

## How to Run

You can run the script in your terminal by navigating to the directory containing the script and running:

```bash
python corpusCounter.py 
```

## Contributing

If you would like to contribute, please feel free to open an issue or pull request.