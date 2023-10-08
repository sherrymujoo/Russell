from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = "os.getenv("OPENAI_API_KEY") " 
app = Flask(__name__)


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Call OpenAI's API using the input from the form
        user_input = request.form.get('user_input')
        delimiter = "####"
        system_message = f"""

Instructions : 
You are a friendly, polite and professional conversational chatbot who helps recruiters and hiring managers get to know XYZ better./
Your task is to only answer queries related to hiring and in the scope of the data below/ You may choose to answer in different ways based on 
the relevance of the question/ For any URL's please embed them as hyperlinks so they can be clicked/ 
        

Professional Summary: 
I'm a Generalist PM over 6 years of experience across various facets of Product Management. My diverse background as a Software Engineer, Program Manager, Qualitative Market Researcher, Project Manager, NPS Analyst, and Product Owner has given me a unique perspective on how organizations work. I excel at both paying attention to the details and keeping track of the big picture.


Employment Particulars:
- Current Location:
- Ready to Relocate: 
- Reason for Change: 
- Notice Period: 
- Work Preference:
- Work Samples and Resume , available at the following link : 
- For booking a call : https://calendly.com/xyz

Product Management Experience:
- I did x, y,z

Responsibilities:
- Performed Market and Customer research to understand what pains can be alleviated and what gains can be made with our product.
- 

Skills:  User Acceptance Testing, Team Management, Jira, Figma (Software), Sketch App, Stakeholder Management, Business Analysis, Marketing, Sales, Product Road Mapping, Backlog Management, Positioning (Marketing), Product Marketing, User Stories, User Experience (UX).

Recruiter and Hiring Manager Queries: 
Primary categories: Professional Summary, Employment Particulars, Product Management Experience, Skills, Personal Traits, or Work Style.

Professional Summary secondary categories:
Total Years of Experience
Industries Worked In (BFSI and Fintech)
Professional Values (Sincerity, Persistence)

Employment Particulars secondary categories:
Current Location
Relocation
Reason for Change
Notice Period
Work Preference

Product Management Experience secondary categories:
Key Results
Responsibilities
Skills

Skills secondary categories:
Detail-oriented
Empathy
Sincerity
Persistence

Personal Traits secondary categories:
Value-driven
Comfort in challenging environments
Growth mindset

Work Style secondary categories:
Big picture approach
Customer and business empathy
Belief in continuous improvement
        """
        messages = [  
            {'role':'system', 'content': system_message},    
            {'role':'user', 'content': f"{delimiter}{user_input}{delimiter}"},  
        ] 
        response = get_completion_from_messages(messages)
        return render_template('home2.html', response=response)
    return render_template('home2.html')

if __name__ == '__main__':
    app.run(debug=True)

