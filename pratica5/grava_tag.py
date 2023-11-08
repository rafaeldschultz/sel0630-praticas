import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#GPIO.setwarnings(False)

leitor = SimpleMFRC522()

texto = "11800945-11800632"

print("Aproxime a tag do leitor para gravar")
leitor.write(texto)
print("Concluido.")

