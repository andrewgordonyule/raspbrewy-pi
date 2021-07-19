from time import strftime, sleep

import RPi.GPIO as GPIO

import gpio_setup
import thermometer


# print out the temperature until the program is stopped

def log_time():
    print('\nStart of Heating cycle at: ' + strftime("%d-%m-%Y %H:%M:%S"))
    print('\nThe temperature is: ')

def start_automation():
    try:
        with open("/home/pi/Desktop/Thermometer/brewing.csv", "a") as log:
            while True:
                print(thermometer.read_temp())
                sleep(60)
                temp_log = thermometer.read_temp()

                # Writes temperature/date to file
                log.write("{0},{1}\n".format(strftime("%d-%m-%Y %H:%M:%S"), str(temp_log)))

                # LED display and heating control

                if temp_log >= 21:
                    # GPIO.output(12, GPIO.HIGH)  # Red LED displays
                    # GPIO.output(32, GPIO.LOW)
                    gpio_setup.switchLightColour(12, GPIO.HIGH, 32, GPIO.LOW)
                    gpio_setup.heatingOff()  # switches plug off

                else:
                    # GPIO.output(32, GPIO.HIGH)  # Blue LED displays
                    # GPIO.output(12, GPIO.LOW)
                    gpio_setup.switchLightColour(32, GPIO.HIGH, 12, GPIO.LOW)
                    gpio_setup.heatingOn()  # switches plug on


    except KeyboardInterrupt:
        gpio_setup.heatingOff()
        GPIO.cleanup()
        print('Program stopped')
        log.close()  # writes to file
        exit()