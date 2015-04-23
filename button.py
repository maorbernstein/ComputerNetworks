import RPi.GPIO as GPIO
import time


def wait_for_edge(pin):
    GPIO.setup(pin,GPIO.IN)
    GPIO.wait_for_edge(pin,GPIO.RISING)
    counter = 0
    while(True):
        print(counter)
        if GPIO.input(pin):
            counter = 0
        else:
            counter += 1
            if counter>5:
                break
        time.sleep(.01)
if __name__ == "__main__":
    print("Waiting")
    wait_for_edge(10)
    print("Done")
