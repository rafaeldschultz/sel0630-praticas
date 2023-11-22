from gpiozero import LED

# Creates a LED object from gpiozero library connected to pin 23
led = LED(23)
# Turns off the LED
led.off()
