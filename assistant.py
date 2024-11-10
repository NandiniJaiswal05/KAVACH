import pyttsx3
import time
import schedule
import requests
from geopy.geocoders import Nominatim

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Function to get weather data
def get_weather():
    api_key = "c55be3e11c0aedd5796e79116d447ac0"
    location = "Current_Location"  # You can replace this with dynamic location if available
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        weather = response["weather"][0]["description"]
        temperature = response["main"]["temp"]
        return f"The current weather is {weather} with a temperature of {temperature}°C."
    else:
        return "Weather data is currently unavailable."

# Function to get location and altitude
def get_location():
    geolocator = Nominatim(user_agent="kavach_assistant")
    location = geolocator.geocode("Your_Current_Coordinates")  # Replace with dynamic coordinates
    altitude = "2500 meters"  # Placeholder for altitude data; replace with sensor data if available
    return f"You are currently at {location.address}, at an altitude of {altitude}."

# Function to get health status (Replace with actual health data)
def get_health_status():
    heart_rate = 75  # Placeholder data
    oxygen_level = 98  # Placeholder data
    return f"Your current heart rate is {heart_rate} BPM and your oxygen level is {oxygen_level}%."

# Function to speak updates
def speak_updates():
    health_status = get_health_status()
    weather_status = get_weather()
    location_status = get_location()

    update_message = (
        f"Health Update: {health_status}. "
        f"Weather Update: {weather_status}. "
        f"Location Update: {location_status}."
    )

    engine.say(update_message)
    engine.runAndWait()

# Schedule the assistant to speak every hour
schedule.every(1).hour.do(speak_updates)

# Main loop to keep the assistant running
if __name__ == "__main__":
    print("KAVACH Voice Assistant is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
