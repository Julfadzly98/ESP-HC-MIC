import machine
import time

# Define the pin connected to the PIR sensor's OUT pin
pir_pin = machine.Pin(15, machine.Pin.IN)  # Assuming GPIO 14 for example, replace with your actual pin

while True:
    pir_value = pir_pin.value()  # Read PIR output value
    print("PIR Value:", pir_value)
    time.sleep(1)

