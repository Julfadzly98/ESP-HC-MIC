import machine
import time

# Define the pin connected to the microphone sensor's AO pin
mic_pin = machine.ADC(machine.Pin(13))  # Assuming GPIO 34 for example, replace with your actual pin

# Define the pin connected to the relay control (IN) pin
relay_pin = machine.Pin(23, machine.Pin.OUT)  # Assuming GPIO 14 for example, replace with your actual pin

def toggle_relay():
    relay_pin.value(1)
    time.sleep(5)
    relay_pin.value(0)

while True:
    mic_value = mic_pin.read()  # Read analog value
    print("Microphone value:", mic_value)

    if mic_value < 500:
        toggle_relay()

    time.sleep(1)

