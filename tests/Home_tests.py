##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Antenna by [Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
import os
import google.generativeai as genai
from dotenv import load_dotenv
import google.generativeai as genai
import logging
from PIL import Image
import streamlit as st
##################################################################################################
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

##################################################################################################
#Environmental variables
load_dotenv()
# genai.configure(api_key=GOOGLE_API_KEY)
# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# google_api_key = os.getenv("GOOGLE_API_KEY")

##################################################################################################
#Check if api key loaded successfully with logging info
# if google_api_key:
#     logger.info("Google API Key loaded successfully.")
# else:
#     logger.error("Failed to load Google API Key.")

##################################################################################################
#Testing Gemini Pro Text Generation with logging info

def model_load_test():
    try:
        model = genai.GenerativeModel('gemini-pro')
        logging.info("Generative model loaded: %s", model)
        
        question = input("Enter the question: ")
        logging.info("User entered question: %s", question)
        
        if question:
            response = model.generate_content(question)
            logging.info("Response generated")
            
            print(response.text)
            logging.info("Response text printed")
        else:
            logging.warning("No question entered")
            print("Please enter a valid question.")
    
    except Exception as e:
        logging.error("An error occurred: %s", str(e))

# Uncomment to test
# model_load_test()
##################################################################################################

#Testing Gemini Pro vision Generation with logging info

def vision_model_load_test():
    try:
        img = Image.open('.src/tushar.png')
        logging.info("Image loaded successfully: %s", img.filename)
        
        if img:
            vision_model = genai.GenerativeModel('gemini-pro-vision')
            logging.info("Generative model loaded: %s", vision_model)
            
            prompt = "Describe image & What is the color of this image and the color of the text?"
            logging.info("Prompt: %s", prompt)
            
            response = vision_model.generate_content([prompt, img])
            logging.info("Response generated")
            
            print(response.text)
            logging.info("Response text printed")
        else:
            logging.warning("Invalid image")
            print("Please enter a valid question.")
    
    except FileNotFoundError as e:
        logging.error("Image file not found: %s", str(e))
    except Exception as e:
        logging.error("An error occurred: %s", str(e))

# Uncomment to test
# vision_model_load_test()
##################################################################################################

#Testing Gemini Pro text with chain with logging info

def text_chain_test():
    try:
        chain_model = genai.GenerativeModel('gemini-pro')
        chat = chain_model.start_chat(history=[])
        logging.info("Generative model and chat initialized successfully")

        question1 = input("Enter the question: ")
        logging.info(f"User entered question: {question1}")
        response = chat.send_message(question1, stream=True)
        response.resolve()
        print(response.text)
        logging.info(f"Response generated for question1: {response.text}")

        # Question2
        question2 = input("Enter the additional question here: ")
        logging.info(f"User entered additional question: {question2}")
        response = chat.send_message(question2, stream=True)
        response.resolve()
        print(response.text)
        logging.info(f"Response generated for question2: {response.text}")

        # print(chat.history)
        return True

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return False

# Uncomment to test
# text_chain_test()
##################################################################################################

#Testing Gemini Pro text with chain with logging info & Configuring the parameters

def text_chain_test_with_config():
    try:
        chain_model = genai.GenerativeModel('gemini-pro')
        chat = chain_model.start_chat(history=[])
        logging.info("Generative model and chat initialized successfully")

        question1 = input("Enter the question: ")
        logging.info(f"User entered question: {question1}")
        generation_config = genai.types.GenerationConfig(max_output_tokens=25, temperature=0.8)
        response = chat.send_message(question1, stream=True, generation_config=generation_config)
        response.resolve()
        print(response.text)
        logging.info(f"Response generated for question1: {response.text}")

        # Question2
        question2 = input("Enter the additional question here: ")
        logging.info(f"User entered additional question: {question2}")
        generation_config = genai.types.GenerationConfig(max_output_tokens=251, temperature=0.8)
        response = chat.send_message(question2, stream=True, generation_config=generation_config)
        response.resolve()
        print(response.text)
        logging.info(f"Response generated for question2: {response.text}")

        # print(chat.history)
        return True

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return False

# Uncomment to test
# text_chain_test_with_config()
##################################################################################################

#Testing Gemini Pro text with chain with logging info & Configuring the parameters

#Testing Application
st.set_page_config(page_title="Antenna",page_icon="♊")
st.write("Welcome to the Gemini Pro Dashboard. You can proceed by providing your Google API Key")

st.sidebar.image('./src/logo.png')
with st.sidebar.expander("Provide Google API Key please"):
     google_api_key = st.text_input("Google API Key", key="google_api_key", type="password")
     
if google_api_key:
    
    logger.info("Google API Key loaded successfully.")
     
if not google_api_key:
    st.info("Enter the Google API Key to continue")
    st.stop()
    
genai.configure(api_key=google_api_key)


###################################################################################
#Multiplemodel selector
with st.sidebar:
    option = st.selectbox('Choose Your Model',('gemini-pro', 'gemini-pro-vision'))

    if 'model' not in st.session_state or st.session_state.model != option:
        st.session_state.chat = genai.GenerativeModel(option).start_chat(history=[])
        st.session_state.model = option
    
    st.write("Adjust Your Parameter Here:")
    temperature = st.number_input("Temperature", min_value=0.0, max_value= 1.0, value =0.5, step =0.01)
    max_token = st.number_input("Maximum Output Token", min_value=0, value =100)
    gen_config = genai.types.GenerationConfig(max_output_tokens=max_token,temperature=temperature)

    st.divider()

    st.markdown("<span ><font size=1>Connect With Me</font></span>",unsafe_allow_html=True)
    "[Linkedin](https://www.linkedin.com/in/tusharaggarwalinseec/)"
    "[GitHub](https://github.com/Towards-GenAI)"
    
    st.divider()
    
    upload_image = st.file_uploader("Upload Your Image Here", accept_multiple_files=False, type = ['jpg', 'png'])
    
    if upload_image:
        image = Image.open(upload_image)

    st.divider()

    if st.button("Clear Chat History"):
        st.session_state.messages.clear()
        
        
#######################################################################################

     


























































