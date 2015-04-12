import RPi.GPIO as GPIO
import time
def wait():
	pin = 4
	GPIO.wait_for_edge(pin,GPIO.RISING)
	while(True):
		x = read(pin)
		if x:
			count = 0
		else:
			count = count + 1
		if count>10:
			break
		time.sleep(.05)

if __name__ =="__main__":
	print("Waiting")
	wait()
	print("Done")
