import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
try:
    while 1:
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()

