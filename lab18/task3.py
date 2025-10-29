import requests

def get_weather():
    api_key = "8ca5cdcf864a96cf6b2f88a3138ca573"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Take city name input from the user
    city_name = input("Enter city name: ")
    
    try:
        # Build full API request URL
        complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"
        
        # Send GET request
        response = requests.get(complete_url)
        response.raise_for_status()
        
        # Parse JSON response
        weather_data = response.json()
        
        # Extract specific details
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        
        # Display results in a user-friendly format
        print("\n--- Weather Details ---")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Network problem (e.g., no internet connection).")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except KeyError:
        print("Error: Could not retrieve weather details. Please check the city name.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
get_weather()