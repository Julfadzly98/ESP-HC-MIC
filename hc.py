import machine
import time

# Define the pins connected to the Ultrasonic Sensor
trig_pin = machine.Pin(12, machine.Pin.OUT)  # Assuming GPIO 14 for example, replace with your actual pin
echo_pin = machine.Pin(13, machine.Pin.IN)   # Assuming GPIO 12 for example, replace with your actual pin
relay_pin = machine.Pin(23, machine.Pin.OUT) 


def toggle_relay():
    relay_pin.value(1)
    time.sleep(40)
    relay_pin.value(0)

def measure_distance():
    # Triggering the Ultrasonic Sensor
    trig_pin.value(1)
    time.sleep_us(10)
    trig_pin.value(0)

    # Waiting for the echo pulse
    while echo_pin.value() == 0:
        pass
    pulse_start = time.ticks_us()

    while echo_pin.value() == 1:
        pass
    pulse_end = time.ticks_us()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration / 58.82  # Speed of sound = 34300 cm/s

    return distance

while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")
#    mic_value = mic_pin.read()  # Read analog value
 #   print("Microphone value:", mic_value)
  #  pir_value = pir_pin.value()  # Read PIR output value
   # print("PIR Value:", pir_value)

    if distance < 500:
        toggle_relay()
        print("Detected!!")

    time.sleep(1)

