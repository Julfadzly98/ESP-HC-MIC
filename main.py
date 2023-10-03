# Import necessary libraries
import machine
import time

# Define pin numbers
pir_pin = 14  # GPIO 14
mic_pin = 15  # GPIO 15
relay_pin = 16  # GPIO 16

# Initialize PIR Sensor
pir = machine.Pin(pir_pin, machine.Pin.IN)

# Initialize Microphone Sensor
mic = machine.Pin(mic_pin, machine.Pin.IN)

# Initialize Relay Module
relay = machine.Pin(relay_pin, machine.Pin.OUT)

# Function to turn on the bulb
def turn_on_bulb():
    relay.on()  # Turn on the relay
    time.sleep(2)  # Keep the relay on for 2 seconds (you can adjust this)

# Main loop
while True:
    if pir.value() == 1 or mic.value() == 1:
        turn_on_bulb()
