# PDF-Merger
Merges multiple PDFs into One. I created this to stop manually merging Science Direct Chapters together.

## Setup 
Set up your virtual python environment
```bash
python3 -m venv .venv
```
Activate your virtual environment 
```bash
source .venv/bin/activate
```
Install the python dependencies
```bash
pip install -r requirements.txt
```

## Usage
You have to have all of the PDFs that you want to merge in the same directory. This script can easily be extended to provide more custom setups but I do not require that so I am keeping this simple.

### Useful Bash Commands
List and sort all the pdfs into human numerical sort. Store the result in a file
```bash
ls *.pdf | sort --human-numeric-sort > pdf_list
```

Provide a file to the script as the list of PDFs to be merged
```bash
cat pdf_list | python3 pdf-merger.pdf
```
