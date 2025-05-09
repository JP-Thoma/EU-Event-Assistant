import streamlit as st
import json
from utils import ask_mistral

st.set_page_config(page_title="EU-Bubble Event Finder", layout="wide")

st.title("EU-Bubble Event Assistant")
st.write("Search and summarize EU events happening in Brussels.")

# Load mock event data
with open("mock_event_data.json", "r") as f:
    events = json.load(f)

query = st.text_input("What kind of events are you interested in?", "Digital policy next week")

if st.button("Search"):
    event_descriptions = "\n".join(
        [f"{e['title']} ({e['date']} at {e['location']}): {e['description']}" for e in events]
    )
    prompt = f"""Here are some EU events:\n\n{event_descriptions}\n\nWhich of these are relevant to: '{query}'? Provide a short summary."""
    
    summary = ask_mistral(prompt)
    st.subheader("Summary")
    st.write(summary)
