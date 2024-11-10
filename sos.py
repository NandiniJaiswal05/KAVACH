import pandas as pd
import asyncio
import bleak
import speech_recognition as sr
import time
import threading
from tkinter import messagebox, Tk
from plyer import notification

# Load the dataset
file_path = r"C:\Users\nandi\Desktop\nandini\Program\HackThisFall\final_data.csv"
data = pd.read_csv(file_path)

# Define thresholds for emergency detection
THRESHOLDS = {
    "SpO2": 85,
    "Heart_Rate": 150,
    "Respiratory_Rate": 30,
    "Body_Temperature": 35.0,
    "Altitude_Sickness": 20,
    "Hypothermia": 30,
    "Dehydration": 25,
    "Cardiovascular": 40
}

# Function to check for emergency based on thresholds
def check_for_emergency(row):
    alert_reasons = []
    if row['Blood Oxygen Saturation (SpO₂, %)'] < THRESHOLDS["SpO2"]:
        alert_reasons.append("Low Blood Oxygen (SpO2)")
    if row['Heart Rate (bpm)'] > THRESHOLDS["Heart_Rate"]:
        alert_reasons.append("High Heart Rate")
    if row['Respiratory Rate (breaths per minute)'] > THRESHOLDS["Respiratory_Rate"]:
        alert_reasons.append("High Respiratory Rate")
    if row['Body Temperature (°C)'] < THRESHOLDS["Body_Temperature"]:
        alert_reasons.append("Low Body Temperature")
    if row['Altitude Sickness (%)'] > THRESHOLDS["Altitude_Sickness"]:
        alert_reasons.append("High Altitude Sickness Risk")
    if row['Hypothermia (%)'] > THRESHOLDS["Hypothermia"]:
        alert_reasons.append("High Hypothermia Risk")
    if row['Dehydration (%)'] > THRESHOLDS["Dehydration"]:
        alert_reasons.append("High Dehydration Risk")
    if row['Cardiovascular Events (%)'] > THRESHOLDS["Cardiovascular"]:
        alert_reasons.append("High Cardiovascular Risk")

    if alert_reasons:
        return True, alert_reasons
    return False, []

# Async function to send SOS alert via Bluetooth using bleak
async def send_sos_bluetooth(message="SOS ALERT: Emergency Detected!"):
    scanner = bleak.BleakScanner()
    devices = await scanner.discover()

    for device in devices:
        print(f"Attempting to send SOS to {device.name} ({device.address})...")
        try:
            async with bleak.BleakClient(device.address) as client:
                if client.is_connected:
                    print(f"Connected to {device.name}.")
                    await client.write_gatt_char("43484152-2dab-3141-6972-6f6861424c45", message.encode())
                    print(f"Message sent to {device.name}.")
        except Exception as e:
            print(f"Failed to send SOS to {device.name}: {e}")

# Pop-up alert for emergencies
def show_popup(message):
    def display_popup():
        root = Tk()
        root.withdraw()
        messagebox.showwarning("Emergency SOS", message)
        root.destroy()

    threading.Thread(target=display_popup).start()

# Notification alert
def send_notification(message):
    notification.notify(
        title="Emergency SOS Alert",
        message=message,
        timeout=5
    )

# Speech detection for "SOS" keyword
def listen_for_sos():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 'SOS' command...")
        audio_data = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio_data).lower()
            if "sos" in command:
                print("SOS command recognized!")
                send_sos()
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")

# Check for emergency from data
def monitor_health_data():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for _, row in data.iterrows():
        emergency, reasons = check_for_emergency(row)
        if emergency:
            message = f"SOS Alert: Detected dangers -> {', '.join(reasons)}"
            print(message)
            loop.run_until_complete(send_sos_bluetooth())  # Call the Bluetooth SOS function asynchronously
            show_popup(message)
            send_notification(message)
        time.sleep(5)  # Delay to simulate real-time monitoring

# SOS activation handler
def send_sos():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_sos_bluetooth())
    send_notification("SOS Alert: An emergency situation has been detected!")
    show_popup("SOS Alert: An emergency situation has been detected!")

# Button press simulation for emergency
def button_press_sos():
    print("SOS Button pressed!")
    send_sos()

# Main function to start threads for monitoring
def start_emergency_system():
    threading.Thread(target=monitor_health_data, daemon=True).start()
    threading.Thread(target=listen_for_sos, daemon=True).start()

    while True:
        button_input = input("Press 'b' for button SOS or 'q' to quit: ")
        if button_input.lower() == 'b':
            button_press_sos()
        elif button_input.lower() == 'q':
            print("Exiting SOS system.")
            break

# Run the emergency system
if __name__ == "__main__":
    start_emergency_system()
