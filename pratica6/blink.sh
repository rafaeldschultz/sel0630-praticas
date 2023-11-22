#!/bin/bash

# This script blinks the LED connected to GPIO18
echo 18 > /sys/class/gpio/export

# The direction of the GPIO must be set to out
echo out > /sys/class/gpio/gpio18/direction

# Blink the LED
while [ 1 ]
	do 
		# Turn on the LED
		echo 1 > /sys/class/gpio/gpio18/value
		# Wait 0.2 seconds
		sleep 0.2s

		# Turn off the LED
		echo 0 > /sys/class/gpio/gpio18/value
		# Wait 0.2 seconds
		sleep 0.2s
	done

