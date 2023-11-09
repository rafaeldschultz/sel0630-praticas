<div align="center">

*Made with:*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Prática 5 

### Introdução a interfaces de visão computacional, sistemas de versionamento de arquivos e controle de acesso via Tags

[Overview](#%EF%B8%8F-overview) •
[Interface de Visão Computacional](#-interface-de-visao-computacional) •
[Controle de acesso via tags](#-controle-de-acesso-via-tags) • 
[Resultados](#-resultados) • 
[Autores](#-autores)

</div>

## ⚡️ Overview

Essa prática contém algoritmos construídos para a simulação de interfaces de visão computacional e controle de acesso via *Tags* utilizando de ```Python``` e da ```Raspberry Pi 3 Model B```.

## 📷 Interface de Visão Computacional

Utilizando de um módulo de câmera para a *raspberry pi* e de um LED, um sistema para reconhecimento facial foi construído. O sistema busca reconhecer pessoas e, ao fazê-lo, um LED é aceso.

Para o controle da câmera e do reconhecimento facial, foi utilizado as bibliotecas```picamera2``` e ```opencv```. Após a configuração da câmera e da criação de um diretório para armazenamento dos rostos reconhecidos, a captura e a tentativa de reconhecimento são feitas da seguinte forma:

```python
# Captura a imagem da camera
im = picam2.capture_array()
# Converte a imagem para tons de cinza
grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# Realiza o reconhecimento de faces
faces = face_detector.detectMultiScale(grey, 1.1, 5)
```

Para cada face detectada, um recorte ao redor desta é realizado e a imagem é salva no diretório ```detected_faces```, no ambiente de execução. 

Além disso, com o reconhecimento um LED também é aceso, o que foi alcançado através da biblioteca ```gpiozero``` e dos métodos ```led.on()``` e ```led.off()```.

## 🪪 Controle de acesso via tags

Utilizando de um módulo ```RFID-RC522``` e de LEDs, um sistema simples de controle de acesso foi desenvolvido. Nesse sistema, o ID fixo de apenas uma das *tags* foi considerado como liberado. A validação se dá da seguinte forma:

* ***Tag* liberada é aproximada do sensor RFID** ➡️ LED verde se acende indicando que o acesso foi liberado; 
* **Qualquer outra *tag* é aproximada do sensor** ➡️ LED vermelho se acende indicando que o acesso foi recusado. 

Tal sistema ilustra o funcionamento básico de sistemas que utilizamos todos os dias, como é o caso do acesso aos prédios do Departamento de Engenharia Elétrica da USP de São Carlos.

O controle do leitor RFID foi feito por meio da biblioteca ```mfrc522```. A leitura do ID da *tag* reconhecida pelo sensor é feita da seguinte forma:

```python
# Cria um objeto da classe 'SimpleMFRC522' para realizacao de leituras.
leitor = SimpleMFRC522()

# ...

# Realiza a leitura do ID da tag e do texto armazenado nela.
id, texto = leitor.read()
```
Já a validação sinalizada pelos LEDs é realizada pela biblioteca ```gpiozero```, da seguinte forma:

```python
# SE o id é igual ao id da tag permitida, libera acesso
if id == allowed:
    # Acende o led verde
    led_green.on()
    print("Acesso permitido!")
# Caso contrário, proibe acesso.
else:
    # Acende LED vermelho.
    led_red.on()
    print("Acesso negado!")
```

## Resultados

Apesar dos algoritmos da biblioteca ```opencv``` serem bastante eficientes, a câmera utilizada na experiência não era de grande qualidade. Assim, grande parte dos rostos reconhecidos pelo algoritmo eram de partes de rostos:

<div align="center">
<img width='600px' src="https://i.imgur.com/WlBZG7A.png"/>
</div>

<br>

Já por parte do leitor RFID, os resultados foram bastante satisfatórios, com reconhecimento preciso das *TAGs*:

![](https://github.com/rafaeldschultz/sel0630-praticas/blob/main/pratica5/RFID.gif)

O funcionamento completo pode ser visualizado em:
* **Reconhecimento Facial:** https://drive.google.com/file/d/1PF6En-GlzKo97FEcxnr1xa8IvLNmZG4d/view?usp=sharing
* **Controle de Acesso:** https://drive.google.com/file/d/1oBpXQ-3HLFVOu1fNlpmXDMI4b2EZ6qbm/view?usp=sharing

## Autores

* **Rafael Dalonso Schultz** - 11800945
* **Ana Julia Aguiar Tagliassachi** - 11800632

Construído com base nos códigos disponibilizados pelo professor Pedro Oliveira, do Departamento de Engenharia Elétrica de São Carlos e nos tutoriais disponibilizados pelas bibliotecas utilizadas.
