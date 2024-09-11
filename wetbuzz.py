import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number you're using
input_pin = 18
buzzer_pin = 16
wet_state = ""

# Set up the pin as an input
GPIO.setup(input_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

def wet_buzz():
    try:
        input_state = GPIO.input(input_pin)
        if(input_state == 0):
            wet_state = "wet"
            GPIO.output(buzzer_pin,1)
        else:
            wet_state = "not wet"
            GPIO.output(buzzer_pin,0)
        
        print("Wet sensor state:", wet_state)
        time.sleep(1)
        return wet_state

    except KeyboardInterrupt:
        GPIO.cleanup()
