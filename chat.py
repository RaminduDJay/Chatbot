import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt, model="gpt-3.5-turbo", max_tokens=50, temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        if 'insufficient_quota' in str(e):
            return "You have exceeded your API quota. Please check your usage and billing details at https://platform.openai.com/account/billing/overview."
        return f"An error occurred: {str(e)}"

def main():
    print("I am Ramindu's assistant. How can I help you?")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get response from GPT
        gpt_response = chat_with_gpt(user_input)
        
        # Print GPT's response
        print(f"AI: {gpt_response}")

if __name__ == "__main__":
    main()
