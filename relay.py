import machine
import time

# Define the pin connected to the relay control (IN) pin
relay_pin = machine.Pin(23, machine.Pin.OUT)  # Assuming GPIO 14 for example, replace with your actual pin


def toggle_relay():
    relay_pin.value(not relay_pin.value())

while True:
    toggle_relay()
    time.sleep(10)
