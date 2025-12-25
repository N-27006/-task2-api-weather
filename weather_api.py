import requests

def get_weather(city):
    api_key = "93af0d6f1d363c115595dc8f8d836b82"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print("\nWeather Details")
            print("----------------")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"])
        else:
            print("City not found. Please try again.")

    except Exception as e:
        print("Error:", e)

# User input (search/filter)
city_name = input("Enter city name: ")
get_weather(city_name)
