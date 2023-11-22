from gpiozero import LED
from time import sleep

# Creates a LED object from gpiozero library connected to pin 23
led = LED(23)

while True:
	# Turns on the LED
	led.on()
	# Waits for 1 second
	sleep(1)
	# Turns off the LED
	led.off()
	# Waits for 1 second
	sleep(1)
