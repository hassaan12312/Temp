import os 
import PyPDF2

def extract_pdf_content(input_file):
    pdf_reader = PyPDF2.PdfReader(input_file)
    full_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        full_text += page_text
    return full_text

def contains_word_from_list(word_list, a_string):
    return any(word in a_string for word in word_list)