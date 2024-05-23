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

#setting model and parameters
def model_load_test():
    model = genai.GenerativeModel('gemini-pro')
    question=input("Enter the question: ")


    if question:
        response = model.generate_content(question)
        print(response.text)
    else:
        print("Please enter a valid question.")

#un comment to test   
#model_load_test()
##################################################################################################

#Testing Gemini Pro vision Generation with logging info

#setting model and parameters
def vision_model_load_test():
    img = Image.open('./tushar.png')
    
    


    if img:
        vision_model = genai.GenerativeModel('gemini-pro-vision')
        response = vision_model.generate_content(img)
        print(response.text)
    else:
        print("Please enter a valid question.")

#un comment to test   
#vision_model_load_test()
##################################################################################################
































































