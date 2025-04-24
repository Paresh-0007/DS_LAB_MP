# ##if everu thing is working, this should be the main page of the app
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# App title
st.markdown("## 🤖 Meet **RealtEase** — your AI real estate genie for Mumbai!")

# API call function
def query_model_api(prompt):
    url = "https://4818-34-143-203-215.ngrok-free.app/chat"  # Replace with your Colab/Ngrok URL
    try:
        response = requests.post(url, json={"prompt": prompt}, timeout=60)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Error contacting model API: {e}"

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/mumbai/res_apartment_dataset.csv")

df = load_data()

# # Suggested Prompts
# st.markdown("#### 💡 Suggested Questions:")
# suggestions = [
#     "What is the average price of a 2 BHK in Andheri?",
#     "Show me a pie chart of property types in Bandra",
#     "How many flats are available in Thane?",
#     "Can you show area vs price trend?",
#     "What do you do?",
#     "Are you always available?"
# ]

# for s in suggestions:
#     if st.button(s):
#         st.session_state["chat_input"] = s

# Session state init
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_query = st.chat_input("Ask me anything about Mumbai real estate...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("RealtEase is thinking..."):
            prompt = f"""You are RealtEase, a real estate assistant trained on Mumbai housing data.
If the query is a question, answer normally.
If the query needs a chart or plot, return Python code only — using pandas and plotly — with no explanation.

Query: {user_query}
Response:"""

            final_resp = query_model_api(prompt)
            if 'df[' not in final_resp:
                final_resp = final_resp.split('Query:')[0].strip()
            print(final_resp)  # Debugging line
            # Check if it's code
            if "import" in final_resp or "df[" in final_resp or "px." in final_resp:
                try:
                    local_vars = {"df": df, "px": px, "st": st}
                    exec(final_resp, {}, local_vars)
                except Exception as e:
                    st.error(f"Error executing code: {e}")
            else:
                st.markdown(final_resp)

        st.session_state.messages.append({"role": "assistant", "content": final_resp})
