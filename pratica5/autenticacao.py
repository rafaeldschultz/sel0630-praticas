from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import LED

led_green = LED(23)
led_red = LED(24)

GPIO.setwarnings(False)

leitor = SimpleMFRC522()

allowed = 771459753502

print("Aproxime a tag do leitor para leitura.")
while True:
	id, texto = leitor.read()
	print(f"ID: {id}")
	print(f"Texto: {texto}")
	
	if id == allowed:
		led_green.on()
		print("Acesso permitido!")
	else:
		led_red.on()
		print("Acesso negado!")
	sleep(3)
	led_green.off()
	led_red.off()
