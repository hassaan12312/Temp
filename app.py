import gradio as gr
from fastapi import FastAPI
from code_processor import process_directory
    
#-----------------------main------------------------
with gr.Row() as demo:
    with gr.Column():
        directory_to_read = gr.Textbox(label = 'Directory path', placeholder = 'Enter Directory path......')
    with gr.Column():
        no_of_candidates = gr.Textbox(label = 'Number of candidates', placeholder = 'Enter number of candidates......')
    with gr.Column():
        job_desc = gr.Textbox(label = 'Job Description', placeholder = 'Enter Job Description......', lines = 10)
        

# Define the Gradio interface
gr.Interface(fn = process_directory, inputs = [directory_to_read, job_desc, no_of_candidates], outputs = gr.HTML(label = 'Output')).launch()

#directory_to_read = "C:/Users/ADMIN/Desktop/Hassaan Docs/test"
#no_of_candidates = input('Enter number of candidates: ')
#job_desc = 
'''
Devsinc is on the lookout for Data Scientists with 6 months - 1.5 years of experience, with a particular focus on machine learning (ML). This role is ideal for individuals who have begun to develop their skills in ML methodologies and are eager to apply this knowledge to solve real-world challenges. The successful candidate will demonstrate a strong foundation in ML techniques, an analytical mindset for unraveling complex data puzzles, and a dedication to contributing to data-driven decisions and innovations.

Responsibilities:

Design, develop, and deploy machine learning models to address specific business challenges. This includes data preprocessing, feature engineering, model selection, training, and validation
Perform exploratory data analysis to uncover hidden patterns, correlations, and insights within structured and unstructured data. Utilize these findings to refine ML models and approaches
Engage with a multidisciplinary team of data scientists, engineers, and business stakeholders to refine data requirements and deliver ML-driven solutions
Create clear visualizations to represent the outcomes of ML models and analyses. Prepare comprehensive reports and presentations that translate complex ML concepts and findings into actionable business insights
Actively pursue learning opportunities in advanced machine learning techniques and algorithms. Incorporate cutting-edge research and tools into projects to enhance model performance and efficiency
Assist in the development of prototypes for predictive models and other ML applications, testing their effectiveness in real-world scenarios
Cross-Functional Application of Insights, Datasets, Code, and Models: Look for opportunities to use insights/datasets/code/models across other functions in the organization (for example in the HR and marketing departments)
Stay curious and enthusiastic about using algorithms to solve problems and enthuse others to see the benefit of your work
Maintain clear and coherent communication, both verbal and written, to understand data needs and report results


Requirements

Bachelor's degree in Data Science, Computer Science, Engineering, Mathematics, Statistics, or a related field with significant coursework or projects in machine learning
A minimum of 6 months -1.5 years of experience in machine learning or data science, with a portfolio demonstrating projects in ML model development, data analysis, and feature engineering. Solid proficiency in ML libraries and frameworks (e.g., TensorFlow, PyTorch, scikit-learn) and programming languages such as Python. Experience with SQL and familiarity with data visualization libraries (e.g., Seaborn, ggplot2)
Exceptional skills in analyzing complex data sets to develop ML models that effectively address business needs
Strong ability to communicate complex ML concepts and the results of analyses clearly to both technical and non-technical stakeholders
Demonstrated ability to work effectively in a team, showing adaptability and openness to feedback


Personal Attributes: 

Passionate about machine learning and its potential to drive innovation and positive change
Eager to learn and stay abreast of the latest advancements in ML technologies and methodologies
Detail-oriented, with a focus on delivering high-quality, accurate ML solutions
'''

#print(process_directory(directory_to_read, job_desc, no_of_candidates))