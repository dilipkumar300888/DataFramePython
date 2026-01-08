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

def get_weather(city):
    """Fetch current weather using Open-Meteo API (no API key needed)."""
    # First, get city coordinates
    print("Fetching coordinates for city...")
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    try:
        geo_res = requests.get(geo_url, timeout=5).json()
        if "results" not in geo_res or len(geo_res["results"]) == 0:
            return "City not found."
        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]

        # Get current weather
        print("/n")
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url, timeout=5).json()
        print("\n")
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]
        print("\n")
        return f"The temperature in {city} is {temp}°C with wind speed {wind} km/h."
    except Exception as e:
        print("Error fetching weather data.")
        return f"Error fetching weather: {e}"

# ------------------ Agent ------------------
def agentic_response(user_input):
    """Decide which tool to use based on input."""
    print("Processing user input...")
    text = user_input.lower()

    if "cat" in text or "fact" in text:
        print("\n")
        return get_cat_fact()
    elif "weather" in text or "temperature" in text:
        # Try to detect city name
        print("Detecting city for weather info...")
        words = text.split()
        city = None
        for i, w in enumerate(words):
            print(f"Word {i}: {w}")
            if w in ["in", "at"] and i + 1 < len(words):
                city = words[i + 1]
                break
        if not city:
            print("City not found in input.")
            return "Please tell me the city, e.g., 'weather in London'."
        return get_weather(city)
    else:
        print("No matching tool found.")
        return "I can give cat facts or weather info. Try 'cat fact' or 'weather in Paris'."

def chatbot():
    print("🐱 Cat Fact Chatbot 🐱")
    print("Type 'fact' to get a cat fact, or 'exit' to quit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Chatbot: Bye! 👋")
            break
        response = agentic_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    print("Starting chatbot...")
    chatbot()
    print("\nChatbot session ended.")