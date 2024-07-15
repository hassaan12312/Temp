import gradio as gr
import regex as re

def extract_text_between_curly_brackets(input_string):
    # Use regular expression to find text between curly brackets
    pattern = r'\{.*?\}'
    matches = re.findall(pattern, input_string)

    # Join the matches into a single string
    extracted_text = ' '.join(matches)

    return extracted_text

def split_string_with_curly_brackets(input_string):
    pattern = r'\{.*?\}'  # Regular expression to match dictionaries
    matches = re.findall(pattern, input_string)
    return [eval(match) for match in matches]

def extract_and_convert_to_integer(input_text):
    try:
        # Extract the value from the Gradio Textbox
        extracted_value = input_text.value

        # Convert the extracted value to an integer
        integer_value = int(extracted_value)
        return integer_value
    except ValueError:
        # Handle invalid input (e.g., non-numeric characters)
        return None
    


def clean_and_sort_candidates(candidate_list):
    cleaned_candidates = []
    for candidate in candidate_list:
        # Remove newline characters from each string
        cleaned_candidate = candidate.replace("\n", "")

        # Extract the score (assuming it's always an integer)
        try:
            score = int(cleaned_candidate.split('"Score": ')[1].split(",")[0])
        except (ValueError, IndexError):
            # Handle invalid or missing score
            score = 0

        cleaned_candidates.append((cleaned_candidate, score))

    # Sort the candidates based on the associated score
    sorted_candidates = sorted(cleaned_candidates, key=lambda x: x[1], reverse=True)

    return [c for c, _ in sorted_candidates]
    
def message_creator(applicants):
    for applicant in applicants:
        print(applicant)
        