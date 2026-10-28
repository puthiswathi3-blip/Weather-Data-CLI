import os
import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_api_key():
    """Get the API key from an environment variable."""
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        print("Error: API key not found.")
        print("Please set the OPENWEATHER_API_KEY environment variable.")
        return None

    return api_key


def get_weather(city, api_key):
    """Fetch weather information for the given city."""
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)

        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city name.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect. Check your internet connection.")
    except requests.exceptions.HTTPError:
        print("Error: Unable to retrieve weather data from the API.")
    except requests.exceptions.RequestException:
        print("Error: An unexpected network error occurred.")
    except ValueError:
        print("Error: Unable to process the weather data.")

    return None


def display_weather(data):
    """Display useful weather information."""
    if not data:
        return

    try:
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        print("\n" + "=" * 35)
        print("         WEATHER REPORT")
        print("=" * 35)
        print(f"City        : {city}, {country}")
        print(f"Condition   : {description}")
        print(f"Temperature : {temperature} °C")
        print(f"Feels Like  : {feels_like} °C")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind_speed} m/s")
        print("=" * 35)

    except (KeyError, IndexError, TypeError):
        print("Error: The weather data format is invalid.")


def main():
    """Run the weather command-line application."""
    print("Welcome to the Weather Data CLI!")

    api_key = get_api_key()

    if not api_key:
        return

    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("Thank you for using the Weather Data CLI!")
            break

        if not city:
            print("Error: City name cannot be empty.")
            continue

        weather_data = get_weather(city, api_key)

        if weather_data:
            display_weather(weather_data)


if __name__ == "__main__":
    main()
