import requests
import json
import os

def get_weather():
    api_key = "8ca5cdcf864a96cf6b2f88a3138ca573"  # 🔑 Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Take city input from user
    city_name = input("Enter city name: ")

    try:
        # Build API URL
        complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

        # Send GET request
        response = requests.get(complete_url)
        response.raise_for_status()

        # Convert to JSON
        weather_data = response.json()

        # Extract important details
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        # Prepare dictionary for this entry
        result = {
            "city": city,
            "temp": temperature,
            "humidity": humidity,
            "weather": description.capitalize()
        }

        # Display formatted JSON in console
        print("\n🌦 Weather Details 🌦")
        print(json.dumps(result, indent=4))

        # File to store results
        file_name = "results.json"

        # Check if file exists; if not, start a new list
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        # Append new result
        data.append(result)

        # Save updated data
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

        print(f"\n✅ Weather data saved to '{file_name}' successfully!")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("⚠ Network error: Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("⏱ The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"⚠ Error occurred: {err}")
    except KeyError:
        print("❌ Could not find weather data. Please check the city name.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
get_weather()