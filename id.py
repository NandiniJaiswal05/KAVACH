import asyncio
from bleak import BleakScanner, BleakClient

async def scan_devices():
    devices = await BleakScanner.discover()
    print("Available Bluetooth devices:")
    for i, device in enumerate(devices):
        print(f"{i}: {device.name} [{device.address}]")
    return devices

async def main():
    devices = await scan_devices()
    try:
        index = int(input("Select the device index (e.g., 0, 1, 2): "))
        device_address = devices[index].address

        async with BleakClient(device_address) as client:
            print(f"Connected to device: {device_address}")

            # Display characteristics
            for service in client.services:
                print(f"Service: {service.uuid}")
                for char in service.characteristics:
                    print(f"  Characteristic: {char.uuid} - {char.properties}")

    except (ValueError, IndexError):
        print("Invalid index. Please enter a valid device index.")
    except Exception as e:
        print(f"Failed to connect: {e}")

# Run the main async function
asyncio.run(main())
