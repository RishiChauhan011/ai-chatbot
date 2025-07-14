import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Error: GEMINI_API_KEY is not set in the environment or .env file.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat()

print("HELLO! What can i do for you?")
print("Type 'exit' to end the chat.")

while True:
    userInput = input("You: ")

    if userInput.lower() == "exit":
        print("Exiting chat. Goodbye!")
        break
    
    response = chat.send_message(userInput)

    print("Gemini:",response.text)