import streamlit as st
from together import Together

TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]
client = Together(api_key=TOGETHER_API_KEY)


#meta-llama/Llama-3.3-70B-Instruct-Turbo-Free #Free
#mistralai/Mistral-7B-Instruct-v0.3 0.2$/M
#mistralai/Mistral-7B-Instruct-v0.2 0.2$/M
def ask_mistral(prompt, model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", temperature=0.7, max_tokens=300):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for EU trainess summarising EU-bubble events in Brussels."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content