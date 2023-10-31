import sys
from Adafruit_BME280 import *
import time
import csv
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection
from sensirion_i2c_sgp4x import Sgp41I2cDevice

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert pascals to inches of mercury (inHg)
def pascals_to_inHg(pascals):
    inHg = pascals * 0.0002953
    return inHg

# Function to read BME280 sensor data
def read_bme280():
    sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    celsius_temperature = sensor.read_temperature()
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

    pascals = sensor.read_pressure()
    inches_of_mercury = pascals_to_inHg(pascals)
    humidity = sensor.read_humidity()

    return fahrenheit_temperature, inches_of_mercury, humidity

# Function to read SGP41 sensor data
def read_sgp41():
    # Initialize the SGP41 sensor device
    with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
        sgp41 = Sgp41I2cDevice(I2cConnection(i2c_transceiver))
        sraw_voc, sraw_nox = sgp41.measure_raw()
        return sraw_voc, sraw_nox

# Create a CSV file and write headers
csv_file = open('sensor_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp', 'Temperature (F)', 'Pressure (inHg)', 'Humidity (%)', 'SRAW VOC', 'SRAW NOx'])

# Main loop to refresh data every 1 minute
while True:
    # Read BME280 sensor data
    fahrenheit_temperature, inches_of_mercury, humidity = read_bme280()

    # Read SGP41 sensor data
    sraw_voc, sraw_nox = read_sgp41()

    # Get the current time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Write data to CSV
    csv_writer.writerow([current_time, fahrenheit_temperature, inches_of_mercury, humidity, sraw_voc, sraw_nox])
    csv_file.flush()  # Flush the buffer to ensure data is written immediately

    print("Last Update: {} | Temp = {:.0f} deg F | Pressure = {:.2f} inHg | Humidity = {:.0f} % | SRAW VOC: {} | SRAW NOx: {}".format(current_time, fahrenheit_temperature, inches_of_mercury, humidity, sraw_voc, sraw_nox))

    
    print("\nWaiting for 1 minute...")
    time.sleep(60)  # Wait for 1 minute before the next reading

# Close the CSV file when the program ends
csv_file.close()
