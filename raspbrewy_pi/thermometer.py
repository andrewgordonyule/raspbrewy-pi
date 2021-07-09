import glob
from time import sleep

# Finds the correct device file that holds the temperature data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


# Function that reads the sensors data
def read_temp_raw():
    f = open(device_file, 'r')  # opens the temp device file
    lines = f.readlines()  # returns the text
    f.close()
    return lines


# Converts the value of the sensor into temperature
def read_temp():
    lines = read_temp_raw()  # read the temp 'device file'

    # while the first line does not contain 'YES', wait for 0.2s
    # and then read the device file again
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()

    # look for the position of '=' in the second line of the
    # device file
    equals_pos = lines[1].find('t=')

    # if the '=' is found, convert the rest of the line after the
    # '=' into degrees Celcuis
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
