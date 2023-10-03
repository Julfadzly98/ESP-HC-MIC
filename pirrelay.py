import machine
import time

# Define the pin connected to the PIR sensor's OUT pin
pir_pin = machine.Pin(15, machine.Pin.IN)  # Assuming GPIO 14 for example, replace with your actual pin

# Define the pin connected to the relay control (IN) pin
relay_pin = machine.Pin(23, machine.Pin.OUT)  # Assuming GPIO 12 for example, replace with your actual pin

def toggle_relay():
    relay_pin.value(1)
    time.sleep(5)
    relay_pin.value(0)

while True:
    pir_value = pir_pin.value()  # Read PIR output value
    print("PIR Value:", pir_value)

    if pir_value == 1:
        toggle_relay()

    time.sleep(1)

