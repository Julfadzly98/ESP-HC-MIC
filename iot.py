import network
from machine import ADC, Pin
import time
import urequests

# Define ADC pins for current and voltage
current_pin = 34  # Example pin for current sensor
voltage_pin = 35  # Example pin for voltage sensor

adc_current = ADC(Pin(current_pin))
adc_voltage = ADC(Pin(voltage_pin))

VREF = 3.3  # Assuming ESP32 uses 3.3V as VREF

# WiFi details
SSID = "smallsaint"  # Replace with your WiFi network name
PASSWORD = "smallsaint"  # Replace with your WiFi network password

WIFI_TIMEOUT = 30  # Maximum time (in seconds) to wait for WiFi connection

# API endpoint for sending data
API_ENDPOINT = "http://example.com/api"  # Replace with your API endpoint

def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        start_time = time.ticks_ms()
        while not sta_if.isconnected():
            if time.ticks_ms() - start_time > WIFI_TIMEOUT * 1000:
                print("Failed to connect to WiFi. Exiting...")
                return False
        print("Connected to WiFi")
        return True
    else:
        print("Already connected to WiFi")
        return True

def read_current():
    # ... (same as before)

def read_voltage():
    # ... (same as before)

def calculate_power(current, voltage):
    # ... (same as before)

def calculate_cost(power, time_used, cost_per_kWh):
    # ... (same as before)

def send_data_to_server(data):
    try:
        response = urequests.post(API_ENDPOINT, json=data)
        response.close()
        print("Data sent successfully")
    except Exception as e:
        print("Failed to send data:", e)

if __name__ == "__main__":
    connected = connect_to_wifi()

    if connected:
        while True:
            current = read_current()
            voltage = read_voltage()
            power = calculate_power(current, voltage)

            # Assuming time_used is in hours
            time_used = 1  # Change this to the actual time used

            cost = calculate_cost(power, time_used, 0.2)  # Change 0.2 to your actual cost per kWh

            data = {
                "current": current,
                "voltage": voltage,
                "power": power,
                "cost": cost
            }

            print(f"Current: {current} A, Voltage: {voltage} V, Power: {power} W, Cost: {cost} Currency")

            send_data_to_server(data)

            time.sleep(3600)  # Sleep for an hour (adjust as needed)
