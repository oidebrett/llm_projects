import ollama
from openai import OpenAI
from dotenv import load_dotenv

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2:1b"
MODEL_GPT = 'gpt-4o-mini'

# set up environment

load_dotenv()
openai = OpenAI()

system_prompt = """
You are an assistant that takes a technical question, and responds with an explanation. 
This is a tool that you will be able to be used by someone during a course on LLM engineering.
"""

def user_prompt_for(question):
    user_prompt = question
    return user_prompt

def messages_for(question):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(question)}
    ]



def answer_question_by_ollama(my_question):
    # And now: call the Ollama API. You will get very familiar with this!
    response = ollama.chat(model=MODEL, messages=messages_for(my_question))
    return response['message']['content']

# Get gpt-4o-mini to answer, with streaming
def answer_question_by_openai(my_question):
    # And now: call the OpenAI API. You will get very familiar with this!
    response = openai.chat.completions.create(model=MODEL_GPT, messages=messages_for(my_question),stream=False)
    #print(response)     
    result = response.choices[0].message.content

    return result

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

print(answer_question_by_ollama(question))
#print(answer_question_by_openai(question))

