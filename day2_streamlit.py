import streamlit as st
from streamlit.logger import get_logger
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

logger = get_logger(__name__)

import os
if os.getenv('USER', "None") == 'appuser': # streamlit
    hf_token = st.secrets['HF_TOKEN']
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token
else:
    # ALSO ADD HERE YOUR PROXY VARS
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["MY_HF_API_TOKEN"]

st.title("Ela, I'm your personal chatGPT, you can ask me everything...")
repo_id = "microsoft/Phi-3-mini-4k-instruct"
temp = 1
print(repo_id, temp)
logger.info(f"{temp=}")

with st.form("sample_app"):
    txt = st.text_area("Enter text:", "what GPT stands for?")
    age = st.slider("How old are you?", 0, 130, 25)
    #st.write("I'm ", age, "years old")
    #my_slide = st.slider("Temp", min_value=0, max_value=2, value=1, step=0.1, format="%0.1f", key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
    sub = st.form_submit_button("submit")
    if sub:
        llm = HuggingFaceEndpoint(
                repo_id=repo_id,  #3.8B model
                task="text-generation",
                temperature=temp
                )
        chat = ChatHuggingFace(llm=llm, verbose=True)
        logger.info("invoking")
        ans = chat.invoke(txt)
        st.info(ans.content)
        logger.info("Done")

