import os
import re
from zipfile import ZipFile

email_regex = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
phone_regex = r'[(]*[0-9]{3}[)]*-[0-9]{3}-[0-9]{4}'
ssn_regex = r'[0-9]{3}-[0-9]{2}-[0-9]{4}'
regexes = [email_regex, phone_regex, ssn_regex]

def find_pii(data):
    matches = []
    for regex in regexes:
        m = re.findall(regex, data)
        matches.extend(m)
    return matches

def print_matches(filedir, matches):
    if len(matches) > 0:
        print(f"PII found in file: {filedir}")
        for match in matches:
            print(match)

def parse_docx(root, docs):
    for doc in docs:
        filedir = os.path.join(root, doc)
        with ZipFile(filedir, 'r') as zip_file:
            with zip_file.open("word/document.xml") as xml_file:
                data = xml_file.read().decode("utf-8")
                matches = find_pii(data)
                print_matches(filedir, matches)

def parse_text(root, txts):
    for txt in txts:
        filedir = os.path.join(root, txt)
        with open(filedir, 'r', encoding="utf-8") as f:
            data = f.read()
            matches = find_pii(data)
            print_matches(filedir, matches)

txt_ext = ['.txt', '.py', '.csv']

def find_files(directory):
    for root, dirs, files in os.walk(directory):
        docx_files = [f for f in files if f.endswith(".docx")]
        if docx_files:
            parse_docx(root, docx_files)
        for ext in txt_ext:
            txt_files = [f for f in files if f.endswith(ext)]
            if txt_files:
                parse_text(root, txt_files)

directory = os.path.join(os.getcwd(), 'Documents')
find_files(directory)
