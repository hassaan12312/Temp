import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
os.environ['GROQ_API_KEY'] = 'Your API key here'

def rate_relevant_candidates(pdf_content, job_desc):
    
    api_key = os.environ.get('GROQ_API_KEY')
    if not api_key:
        raise ValueError("Please set the GROQ_API_KEY environment variable.")
    

    delimiter = '```'
    text_data = "You are an excellent CV shortlister. Follow the instructions stricly and be consistent in your outputs. Give me the response in a JSON format with keys 'Name' and 'Score' and 'Reason of Score'. Example of response: {'Name': 'Hassaan', 'Score': 10, 'Reason of Score': 'Lacks Experience'}. Analyze the text between the delimiters where the delimiters are three backticks. You have to intelligently match CV with the given Job Description and focus on scoring. Give score out of 100 on basis of suitability of the candidate to the job description provided. Make sure to be very strict in your scoring. Provide reason for your scoring as well in no more than 3 lines. Do not provide any other information apart from the one requested. Remember to be very very strict for the scoring"
    human_message = f"Job Description: {job_desc}\nResume Details: {pdf_content}"
    client = Groq(api_key = api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":f"{human_message}{delimiter}{text_data}{delimiter}"
            }
        ],
        model = "llama3-70b-8192"
    )
    
    
    return chat_completion.choices[0].message.content
