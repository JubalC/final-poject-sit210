import RPi.GPIO as GPIO
import time
from gpiozero import MotionSensor
import requests

pir = MotionSensor(14)

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

counter = 0

def callback(channel):
	if GPIO.input(channel):
		global counter
		print("sound detected")
		counter += 1
		print(counter)
	else:
		print("sound detected")
		
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime= 300)
GPIO.add_event_callback(channel, callback)

while True:
	time.sleep(1)
	pir.wait_for_motion()
	counter += 1
	print(counter)
	print("You moved")
	if counter >= 10:
		requests.post('https://maker.ifttt.com/trigger/activity_sensed/with/key/bShBBprGVr09zEYq6nH_Bl')
		counter = 0
		print(counter)
	pir.wait_for_no_motion()
