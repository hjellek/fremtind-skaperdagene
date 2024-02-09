import os
import glob
import time

# Define the path to the DS18B20 sensor data file
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Function to read sensor data
def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

# Function to parse temperature data
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

# Main program
while True:
    temp_c, temp_f = read_temp()
    print('Temperature:', temp_c, 'C', temp_f, 'F')
    time.sleep(1)