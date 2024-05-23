##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Antenna[Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
import os
import google.generativeai as genai
from dotenv import load_dotenv
import google.generativeai as genai
import logging
from PIL import Image
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


google_api_key = os.getenv("GOOGLE_API_KEY")

##################################################################################################
#Check if api key loaded successfully with logging info
if google_api_key:
    logger.info("Google API Key loaded successfully.")
else:
    logger.error("Failed to load Google API Key.")

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
text_chain_test_with_config()
##################################################################################################

#Testing Gemini Pro text with chain with logging info & Configuring the parameters





























































