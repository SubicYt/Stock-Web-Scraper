from groq import Groq
import pandas as pd
import kaggle

# Download latest version
#path = kaggle.dataset_download("borismarjanovic/price-volume-data-for-all-us-stocks-etfs")
"""TO-DO - Fine tune Model, experimentation in GroqCloud"""

client = Groq(api_key="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")

def chat_with_model():
    print("Welcome to The Congress Trade Tracker Chat!")
    print("Type 'exit' to quit the chat.\n")
    
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("\nResponse: Goodbye!\n")
            break
        
        try:
            # User input
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": user_input}]
            )
            # Display the model's response
            print(f"\nResponse: {response.choices[0].message.content}\n")
        except Exception as e:
            print(f"Error: {e}\n")

def process_data():
    pass
  

if __name__ == "__main__":
    chat_with_model()

