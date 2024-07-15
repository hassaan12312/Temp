import os
from pdf_handler import extract_pdf_content
from candidate_selector import rate_relevant_candidates
from string_editors import clean_and_sort_candidates, extract_text_between_curly_brackets, split_string_with_curly_brackets

def list_to_html(data_list):
    """
    Converts a list of dictionaries to an HTML representation with each item in a separate <div>.

    Args:
        data_list (list[dict]): List of dictionaries containing data.

    Returns:
        str: HTML representation.
    """
    html_output = ""
    for item in data_list:
        html_output += "<div style='border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; font-size: 35px'>\n"
        html_output += "<div>\n"
        html_output += f"<strong>Name:</strong> {item['Name']}<br>\n"
        html_output += f"<strong>Score:</strong> {item['Score']}<br>\n"
        html_output += f"<strong>Reason of Score:</strong> {item['Reason of Score']}<br>\n"
        html_output += "</div>\n"
    
        html_output += "</div>\n"
    return html_output

def process_directory(directory_path, job_desc, no_of_candidates):
    
    candidates_results = []
    no_of_candidates = int(no_of_candidates)
    
    try:
        count = 0
        
        pdf_files = [file for file in os.listdir(directory_path) if file.lower().endswith(".pdf")]
        for pdf_file in pdf_files:
            pdf_path = os.path.join(directory_path, pdf_file)
            with open(pdf_path, "rb") as pdf_file_obj:
                content = extract_pdf_content(pdf_file_obj)
                suitability_result = rate_relevant_candidates(content, job_desc)
                candidates_results.append(suitability_result)
                print(suitability_result)
                count += 1
                print("Number of pdf files read: ", count)

        candidates_results = clean_and_sort_candidates(candidates_results)
        sentences = ""
        for x in candidates_results:
            sentences += x
        
        sentences = extract_text_between_curly_brackets(sentences)
        sentences = split_string_with_curly_brackets(sentences)
        
        sorted_applicants = sorted(sentences, key=lambda x: x['Score'], reverse=True)
        #print(sorted_applicants)
        selected_applicants = sorted_applicants[:no_of_candidates]
        print(selected_applicants)
        list_html = list_to_html(selected_applicants)
        return list_html
        
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
        return