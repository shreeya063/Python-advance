import requests

# Taking Input from Front-end user
api_key = input("Enter your API key here: ")
city_name = input("Enter city name to find info: ").capitalize()

# My api key { 568785a124ed1b436de8f3c95475adc2 }

# Processing request using Open Weather API server
request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response = requests.get(request).json()

# Check if the city is valid
if response.get("cod") != 200:
    print(f"Error: {response.get('message')}")
else:
    # Getting Desired information from API
    temp_in_kelvin = response["main"]["temp"]
    description = response["weather"][0]["description"]
    
    # Convert Kelvin to Celsius
    celsius = temp_in_kelvin - 273.15  # Corrected conversion formula
    
    # Print the results
    print(f"The city is: {city_name}, Temperature: {round(celsius, 1)} °C. The weather condition is: {description}.")
