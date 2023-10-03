import machine
import time

# Define the pin connected to the microphone sensor's AO pin
mic_pin = machine.ADC(machine.Pin(13))  # Assuming GPIO 34 for example, replace with your actual pin

while True:
    mic_value = mic_pin.read()  # Read analog value
    print("Microphone value:", mic_value)
    time.sleep(1)
    
    

