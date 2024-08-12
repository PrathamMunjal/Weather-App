import requests

def get_weather(lat, lon, api_key):
    try:
        # Make the request to the weather API
        response = requests.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params={'lat': lat, 'lon': lon, 'appid': api_key},
            verify=False  # Disable SSL verification (for debugging only)
        )
        
        # Check if the request was successful
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Print the response status code and JSON data for debugging
        print(f"Status Code: {response.status_code}")
        print("Response JSON:", response.json())
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Print detailed error message
        print(f"An error occurred: {e}")

# Example usage
lat = 29.1562688
lon = 75.7292303
api_key = '19e91db32a1408d67ceac97e7a40eca1'
weather_data = get_weather(lat, lon, api_key)
if weather_data:
    print("Weather Data:", weather_data)
else:
    print("Failed to retrieve weather data.")
