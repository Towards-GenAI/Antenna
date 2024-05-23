##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Antenna[Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging
from PIL import Image
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import json
#From src
from src.components.navigation import *
##################################################################################################
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

##################################################################################################
#Environmental variables
# load_dotenv()

# google_api_key = os.getenv("GOOGLE_API_KEY")
##################################################################################################

# Load chat history from file if it exists
def load_chat_history():
    if os.path.exists("chat_history.json"):
        with open("chat_history.json", "r") as f:
            return json.load(f)
    return []

# Save chat history to file
def save_chat_history(chat_history):
    with open("chat_history.json", "w") as f:
        json.dump(chat_history, f)
##################################################################################################
# Antenna Application flow
page_config("Antenna", "♊", "wide")
custom_style()


st.title("♊Antenna♊")
st.markdown('''
        <style>
            div.block-container{padding-top:0px;}
            font-family: 'Roboto', sans-serif; /* Add Roboto font */
            color: blue; /* Make the text blue */
        </style>
            ''',
        unsafe_allow_html=True)
st.markdown(
    """
    ### A Text & Image Chatbot by [Towards-GenAI](https://github.com/Towards-GenAI)
    """
)

def main():
    
    st.sidebar.image('./src/logo.png')
    with st.sidebar.expander("Google API Key please"):
        google_api_key = st.text_input("Google API Key", key="google_api_key", type="password")
         
    if google_api_key:
        logger.info("Google API Key loaded successfully.")
    else:
        st.info("Enter the Google API Key to continue")
        st.stop()
        
    genai.configure(api_key=google_api_key)

    # Model selector
    with st.sidebar:
        option = st.selectbox('Model', ('gemini-pro', 'gemini-pro-vision'))

        if 'model' not in st.session_state or st.session_state.model != option:
            st.session_state.chat = genai.GenerativeModel(option).start_chat(history=[])
            st.session_state.model = option
        
        st.write("Adjust Parameters Here:")
        temperature = st.number_input("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        max_token = st.number_input("Maximum Output Token", min_value=0, value=251, max_value=1500)
        gen_config = genai.types.GenerationConfig(max_output_tokens=max_token, temperature=temperature)

        st.divider()

        if st.button("Clear Chat History"):
            st.session_state.messages.clear()
            save_chat_history([])
        
        st.divider()
        
        upload_image = st.file_uploader("Upload Your Image Here", accept_multiple_files=False, type=['jpg', 'png'])
        
        if upload_image:
            image = Image.open(upload_image)

        st.divider()

        
       
        footer()
            
    # Load chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = load_chat_history()

    # Display chat messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Handle user input
    if upload_image:
        if option == "gemini-pro":
            st.info("Please switch to the Gemini Pro Vision model to use image input.")
            st.stop()
        prompt = st.chat_input()
        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = st.session_state.chat.send_message([prompt, image], stream=True, generation_config=gen_config)
            response.resolve()
            msg = response.text

            st.session_state.chat = genai.GenerativeModel(option).start_chat(history=[])
            st.session_state.messages.append({"role": "assistant", "content": msg})
            
            st.image(image, width=300)
            st.chat_message("assistant").write(msg)
    else:
        prompt = st.chat_input()
        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            response = st.session_state.chat.send_message(prompt, stream=True, generation_config=gen_config)
            response.resolve()
            msg = response.text
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)

    # Saving chat history
    save_chat_history(st.session_state.messages)
    


if __name__ == "__main__":
    main()
