# KAVACH - Mountain Climber Safety System # 

KAVACH is a fully functioning IoT-based safety system designed to assist mountain climbers in managing health risks, weather conditions, navigation, and communication. It integrates hardware with AI and software to provide real-time updates, emergency communication, health risk prediction, and more. Developed by a team of first-time coders, KAVACH is an innovative project that uses smartwatch sensors, Bluetooth mesh networking, and a voice-based assistant to enhance climbers' safety.

## Features

- **Health Risk Prediction:** Monitors heart rate, SpO2, and other health metrics to predict potential health risks in high-altitude environments.
- **Weather Updates:** Provides real-time weather updates and warnings based on location to help climbers make informed decisions.
- **Bluetooth Mesh Network:** Enables communication between co-climbers without relying on external cellular networks, ensuring connectivity even in remote areas.
- **SOS Alerts:** Sends emergency alerts with GPS coordinates to rescuers, even in low-connectivity regions.
- **Navigation & Route Suggestions:** Suggests optimal trails and alternative routes based on real-time location data.
- **Voice-Based Assistant:** Provides hands-free updates on health status, location, weather, and more, ensuring safety while keeping the climber's focus on the climb.

## Installation

### Prerequisites

- Smartwatch with built-in sensors (heart rate, GPS, SpO2)
- Raspberry Pi (for processing and Bluetooth connectivity)
- Python 3.x
- Bluetooth-enabled devices

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/kavach.git
2. Navigate the directory:
   cd kavach

###How It Works

- The system collects health data (heart rate, SpO2) from the smartwatch and processes it to predict potential health risks.
- Weather data is fetched from an API and delivered to the climber in real-time.
- The Bluetooth mesh network is used for communication between co-climbers, ensuring that they stay connected even without cellular service.
- The voice assistant continuously provides updates on health, weather, location, and navigation. 

### Acknowledgements
- GitHub Education: For supporting and encouraging the use of GitHub as a collaborative platform.
-Raspberry Pi: For providing the platform for integrating hardware and software.
- Smartwatch API documentation: For enabling seamless sensor integration.
