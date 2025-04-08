##if everu thing is working, this should be the main page of the app
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# App title
st.markdown("## 🤖 Meet **RealtEase** — your AI real estate genie for Mumbai!")

# API call function
def query_model_api(prompt):
    url = "https://833b-35-247-3-156.ngrok-free.app/chat"  # Replace with your Colab/Ngrok URL
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



# import streamlit as st
# import pandas as pd
# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
# import plotly.express as px

# # Title and Chatbot Name
# st.markdown("## 🤖 Meet **RealtEase** — your AI real estate genie for Mumbai!")

# # Load the fine-tuned model & tokenizer
# @st.cache_resource
# def load_model():
#     tokenizer = AutoTokenizer.from_pretrained("./mistral-realestate-qlora/checkpoint-441")
#     model = AutoModelForCausalLM.from_pretrained("./mistral-realestate-qlora/checkpoint-441", torch_dtype=torch.float16, device_map="auto")
#     pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
#     return pipe

# pipe = load_model()

# # Load your dataset
# @st.cache_data
# def load_data():
#     return pd.read_csv("data/mumbai/res_apartment_dataset.csv")

# df = load_data()

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

# # Chat Interface
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Show chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # Input box
# user_query = st.chat_input("Ask me anything about Mumbai real estate...")

# if user_query:
#     st.session_state.messages.append({"role": "user", "content": user_query})
#     with st.chat_message("user"):
#         st.markdown(user_query)

#     with st.chat_message("assistant"):
#         with st.spinner("RealtEase is typing..."):
#             prompt = f"""You are RealtEase, a real estate assistant trained on Mumbai housing data.
# If the query is a question, answer normally.
# If the query needs a chart or plot, return Python code only — using pandas and plotly — with no explanation.

# Query: {user_query}
# Response:"""

#             response = pipe(prompt, max_new_tokens=512, do_sample=True, temperature=0.5)[0]['generated_text']
#             final_resp = response.split("Response:")[-1].strip()

#             # Decide if it's code or not
#             if "import" in final_resp or "px." in final_resp or "df[" in final_resp:
#                 try:
#                     # Define df in local scope
#                     local_vars = {"df": df, "px": px, "st": st}
#                     exec(final_resp, {}, local_vars)
#                 except Exception as e:
#                     st.error(f"Error executing code: {e}")
#             else:
#                 st.markdown(final_resp)

#         st.session_state.messages.append({"role": "assistant", "content": final_resp})
