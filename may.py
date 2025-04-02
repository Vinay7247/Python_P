# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()
# client = Groq(
#     api_key=os.environ.get("GROUP_API_KEY"),
# )
# prompt = input("Enter your question: ")
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": prompt ,
#         }
#     ],
#     model="deepseek-r1-distill-llama-70b",
# )

# print(chat_completion.choices[0].message.content)




import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROUP_API_KEY"),
)

# Set up Streamlit page configuration
st.set_page_config(page_title="Groq Chat Assistant", page_icon="💬")
st.title("Groq Chat Assistant")

# Create a text input for user questions
user_input = st.text_input("Enter your question:", key="user_input")

# Add a button to submit the question
if st.button("Send"):
    if user_input:
        # Show a spinner while processing
        with st.spinner("Generating response..."):
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="deepseek-r1-distill-llama-70b",
            )
            
            # Display the response
            st.write("Response:")
            st.write(chat_completion.choices[0].message.content)
    else:
        st.warning("Please enter a question!")
