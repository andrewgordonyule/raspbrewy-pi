from time import strftime

# print out the temperature until the program is stopped

print('\nStart of Heating cycle at: ' + strftime("%d-%m-%Y %H:%M:%S"))
print('\nThe temperature is: ')

try:
    with open("/home/pi/Desktop/Thermometer/brewing.csv", "a") as log:
        while True:
            print(read_temp())
            sleep(60)
            temp_log = read_temp()

            # Writes temperature/date to file
            log.write("{0},{1}\n".format(strftime("%d-%m-%Y %H:%M:%S"), str(temp_log)))

            # LED display and heating control

            if read_temp() >= 21:
                GPIO.output(12, GPIO.HIGH)  # Red LED displays
                GPIO.output(32, GPIO.LOW)
                heatingOff()  # switches plug off

            else:
                GPIO.output(32, GPIO.HIGH)  # Blue LED displays
                GPIO.output(12, GPIO.LOW)
                heatingOn()  # switches plug on


except KeyboardInterrupt:
    heatingOff()
    GPIO.cleanup()
    print('Program stopped')
    log.close()  # writes to file
    exit()
