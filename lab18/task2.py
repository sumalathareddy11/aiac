import requests
import json

def get_weather():
    api_key = "8ca5cdcf864a96cf6b2f88a3138ca573"  # Replace with your actual OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Take input from the user
    city_name = input("Enter city name: ")
    
    try:
        # Construct the full API URL
        complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"
        
        # Send GET request
        response = requests.get(complete_url)
        
        # Raise error if the request failed
        response.raise_for_status()
        
        # Convert response to JSON
        weather_data = response.json()
        
        # Display JSON output
        print("\nWeather Details (JSON format):")
        print(json.dumps(weather_data, indent=4))
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Network problem (e.g., no internet connection).")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
get_weather()