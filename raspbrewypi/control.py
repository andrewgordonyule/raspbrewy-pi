from time import strftime, sleep

import RPi.GPIO as GPIO

import gpio_setup, graphing, thermometer


# print out the temperature until the program is stopped

def log_time():
    print('\nStart of Heating cycle at: ' + strftime("%d-%m-%Y %H:%M:%S"))
    print('\nThe temperature is: ')


def start_automation():

    log_time()

    try:
        with open("/home/pi/Desktop/Thermometer/brewing.csv", "a") as log:
            while True:
                print(thermometer.read_temp())
                sleep(60)
                temp_log = thermometer.read_temp()
                current_time = strftime("%H:%M:%S")

                # Writes temperature/date to file
                log.write("{0},{1}\n".format(strftime("%d-%m-%Y %H:%M:%S"), str(temp_log)))

                # Draws temperature graph
                graphing.plot_graph(temp_log, current_time)

                # LED display and heating control
                if temp_log >= 21:
                    gpio_setup.switchLightColour(12, GPIO.HIGH, 32, GPIO.LOW) # Red LED on
                    gpio_setup.heatingOff()  # switches plug off

                else:
                    gpio_setup.switchLightColour(32, GPIO.HIGH, 12, GPIO.LOW) # Blue LED on
                    gpio_setup.heatingOn()  # switches plug on


    except KeyboardInterrupt:
        gpio_setup.heatingOff()
        GPIO.cleanup()
        print('Program stopped')
        log.close()  # writes to file
        exit()


if __name__ == "__main__":
    start_automation()
