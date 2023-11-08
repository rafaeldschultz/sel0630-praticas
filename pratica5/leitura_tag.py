from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

leitor = SimpleMFRC522()

print("Aproxime a tag do leitor para leitura.")
while True:
	id, texto = leitor.read()
	print(f"ID: {id}")
	print(f"Texto: {texto}")
	sleep(3)

