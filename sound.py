import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the pin number connected to the sensor
sensor_pin = 17
loop_duration = 10

# Setup the GPIO pin as input
GPIO.setup(sensor_pin, GPIO.IN)

SERVO_PIN = 20

class ServoMotor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SERVO_PIN,GPIO.OUT)
        self.servo = GPIO.PWM(SERVO_PIN, 50)  # GPIO 17 for servo with 50Hz frequency
        self.servo.start(0)

    def rotate(self, angle):
        duty = angle / 18 + 2
        self.servo.ChangeDutyCycle(duty)
        time.sleep(0.5)

    def stop(self):
        self.servo.stop()
        GPIO.cleanup()

serv = ServoMotor()

def sound_serv():
    try:
        # Read the digital input value
        sensor_value = GPIO.input(sensor_pin)
        
        # Print the sensor value
        print("Sound Sensor value:", sensor_value)
        
        # Wait for a short time before reading again
        time.sleep(1)
        count = 0
        if sensor_value == 0:
                
                while count < 10:
                        # Rotate servo motor by 90 degrees
                        serv.rotate(90)
                        # Rotate servo motor back to initial position (0 degrees)
                        serv.rotate(0)
                        time.sleep(1)
                        count += 1

    except KeyboardInterrupt:
        print("\nExiting program...")
        serv.stop()
        GPIO.cleanup()
