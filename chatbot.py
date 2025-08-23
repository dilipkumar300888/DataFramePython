import requests

def get_cat_fact():
    """Fetch a random cat fact from the public API."""
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error if HTTP request failed
        data = response.json()
        return data.get("fact", "Couldn't fetch fact.")
    except Exception as e:
        return f"Error: {e}"

def chatbot():
    print("🐱 Cat Fact Chatbot 🐱")
    print("Type 'fact' to get a cat fact, or 'exit' to quit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Chatbot: Bye! 👋")
            break
        elif user_input == "fact":
            fact = get_cat_fact()
            print(f"Chatbot: {fact}")
        else:
            print("Chatbot: I can only give cat facts. Type 'fact' or 'exit'.")

if __name__ == "__main__":
    print("Starting chatbot...")
    chatbot()