#!/bin/bash

# This script turns off the LED connected to GPIO18
echo 18 > /sys/class/gpio/export

# The direction of the GPIO must be set to out
echo out > /sys/class/gpio/gpio18/direction

# Turn off the LED
echo 0 > /sys/class/gpio/gpio18/value
