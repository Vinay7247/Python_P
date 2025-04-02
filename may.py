import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(
    api_key=os.environ.get("GROUP_API_KEY"),
)
prompt = input("Enter your question: ")

text = f"you are a financial expert AI assistant. your task is a provide accurate and insightful response to the following user query related to finance :{prompt} .other than finance Questions respond with ' i don't know"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": text ,
        }
    ],
    model="llama-3.3-70b-specdec",
)

print(chat_completion.choices[0].message.content)