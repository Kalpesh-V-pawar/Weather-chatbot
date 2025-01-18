import requests

# Function to get weather data
def get_weather(city):
    # Replace with your OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }

    # Make the API request
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract weather information
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            return f"The weather in {city} is '{weather}' with a temperature of {temp}°C (feels like {feels_like}°C)."
        else:
            return f"Could not fetch weather data for '{city}'. Please check the city name."
    except Exception as e:
        return "Error: Unable to fetch weather data. Please try again later."

# Weather chatbot function
def weather_chatbot():
    print("Weather Chatbot: Hi! I can provide you with the current weather. Type 'exit' to end the chat.")
    
    while True:
        # Get user input
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Weather Chatbot: Goodbye! Stay safe!")
            break
        else:
            # Assume the user input is a city name
            weather_response = get_weather(user_input)
            print(f"Weather Chatbot: {weather_response}")

# Run the chatbot
if __name__ == "__main__":
    weather_chatbot()
