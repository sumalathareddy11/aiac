import requests
import json

def get_weather(city_name):
    api_key = "8ca5cdcf864a96cf6b2f88a3138ca573"  # Your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Construct full URL
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"
    
    try:
        # Send GET request
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Convert response to JSON
        weather_data = response.json()
        
        if weather_data["cod"] == 200:
            # Extract main weather information
            main_data = weather_data["main"]
            weather_description = weather_data["weather"][0]["description"]
            
            # Create a formatted output
            weather_info = {
                "city": city_name,
                "temperature": main_data["temp"],
                "humidity": main_data["humidity"],
                "pressure": main_data["pressure"],
                "description": weather_description
            }
            
            # Display weather details in JSON format
            print(json.dumps(weather_info, indent=4))
        else:
            print(f"Error: Could not find weather data for {city_name}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except KeyError as e:
        print(f"Error parsing weather data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        if city:
            get_weather(city)
        else:
            print("Please enter a valid city name.")

# Run the program
if __name__ == "__main__":
    main()