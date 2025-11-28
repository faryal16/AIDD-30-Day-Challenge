from openagents.llms.gemini import Gemini
import os

# Ideally, the API key should be stored in a more secure way, 
# but for this example, we'll use an environment variable.
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Initialize the Gemini model
llm = Gemini(model="gemini-pro", api_key=GEMINI_API_KEY)

def generate_summary(text):
    """
    Generates a summary of the given text using the Gemini model.
    """
    prompt = f"Please summarize the following text:\n\n{text}"
    
    response = llm.call(prompt)
    return response

def generate_quiz(text):
    """
    Generates a quiz based on the given text using the Gemini model.
    """
    prompt = f"Based on the following text, generate a multiple-choice quiz with 5 questions. For each question, provide 4 options and indicate the correct answer:\n\n{text}"
    
    response = llm.call(prompt)
    return response
