import requests
import pyttsx3
import json

# Function to interact with Warp API
def ask_warp(prompt):
    url = "http://localhost:11434/api/generate"  # Make sure the port matches your Warp server's configuration
    payload = {
        "model": "llama3",  # or whichever model you're using
        "prompt": prompt,
        "stream": False
    }

    try:
        # Make the request to the Warp API
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Check if the request was successful

        # Parse the response
        result = response.json()
        
        # Handle cases where 'response' might not exist
        if "response" in result:
            return result["response"]
        else:
            return "Sorry, I didn't get a valid response from Warp."

    except requests.exceptions.RequestException as e:
        # Handle request exceptions such as connection errors
        return f"Error: Could not connect to Warp API. {e}"

# Text-to-speech function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to start the assistant and greet the user
def greet_user():
    greeting = "Hello Boss. How can I assist you today?"
    speak(greeting)  # Let the assistant speak
    print(greeting)  # Display the greeting in the terminal

# Example usage in the main function
if __name__ == "__main__":
    greet_user()

    # Simulating the assistant asking for user input
    user_input = input("🟢 Command me:\n> ").lower()

    # Example: Using ask_warp to generate a response
    prompt = f"You are an assistant. Answer the question: {user_input}"
    response = ask_warp(prompt)

    print(f"🤖 Warp says: {response}")
    speak(response)  # Let the assistant speak the response
