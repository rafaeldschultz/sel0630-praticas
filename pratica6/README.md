<div align="center">

*Made with:*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Prática 6

### Gerenciamento de Serviços Personalizados em Sistemas Embarcados

[Overview](#%EF%B8%8F-overview) •
[Piscando LED com bash](#-piscando-led-com-bash) •
[Piscando LED com Python](#-piscando-led-com-python) • 
[Resultados](#-resultados) • 
[Autores](#-autores)

</div>

## ⚡️ Overview

Essa prática contém algoritmos construídos para serem adicionados a uma unidade de serviço personalizada (*systemd service unit*) com inicialização durante o *boot* do sistema operacional. Os algoritmos foram construídos em ```python``` e em ```bash``` e foram simulados em uma ```Raspberry Pi 3 Model B```.

## ⌨ Piscando LED com bash

Inicialmente, um LED branco foi conectado a porta ```GPIO 18``` de modo que este piscasse com período de $0,2s$. 

O controle do estado do LED é feito por meio dos comandos abaixo, e o código completo pode ser visualizado em ```blink.sh```. 

```bash
#blink.sh
# ...

# Turn on the LED
echo 1 > /sys/class/gpio/gpio18/value

# Turn off the LED
echo 0 > /sys/class/gpio/gpio18/value
```

Também foi construído o script ```blinkoff.sh``` para desligar o LED, que será sempre executado quando esse serviço for finalizado.

Para adicionar o serviço criado ao ```systemd```, inicialmente foi-se desenvolvido o script ```blink.service```. A associação do serviço com os scripts ```bash``` a serem executados é dada pelas linhas abaixo, em que o script ```ExecStart``` é executado a partir do momento em que o serviço é iniciado até o momento em que for finalizado, e o script ```ExecStop``` é executado quando o serviço for finalizado.

```yaml
[Service]
ExecStart=/home/sel/4532/praticas/pratica6/blink.sh
ExecStop=/home/sel/4532/praticas/pratica6/blinkoff.sh
user=SEL
```

Para executar esse código em outra máquina, é necessário alterar o caminho dos scripts para o equivalente na máquina que irá executar o processo.

Por fim, o arquivo ```blink.service``` foi copiado para a pasta de serviços do ```systemd``` (```/lib/systemd/system/```) e o serviço foi habiliado durante a inicialização com o comando ```sudo systemctl enable blink```.


## 🐍 Piscando LED com Python

De forma similar ao anterior, os scripts ```blink_led.py``` e ```blink_off.py``` foram construídos para piscarem um LED conectado a porta ```GPIO 23``` com período de $1s$ durante a inicialização. 

O controle do LED é feito através da biblioteca ```gpiozero``` e dos métodos ```led.on()``` e ```led.off()```. O arquivo ```blink_led.py``` é similar ao desenvolvido em ```blinkoff.sh```, enquanto o arquivo
 ```blink_off.py``` é similar ao visto em ```blinkoff.sh```.

Para adicionar o serviço criado ao ```systemd```, desenvolveu-se o script ```blink_python.service```, no qual a sua associação com os scripts ```python``` desenvolvidos é realizada pelas linhas:

```yaml
[Service]
ExecStart=/usr/bin/python3 /home/sel/4532/praticas/pratica6/blink_led.py
ExecStop=/usr/bin/python3 /home/sel/4532/praticas/pratica6/blink_off.py
user=SEL
```

Repare que aqui inicialmente indica-se o caminho do binário do ```python```, que será responsável por executar o script do LED.

Igualmente para esse código, se desejar executá-lo é necessário alterar o caminho dos scripts para o equivalente na máquina que irá executar o processo.

Por fim, o arquivo ```blink_python.service``` foi copiado para a pasta de serviços do ```systemd``` (```/lib/systemd/system/```) e o serviço foi habiliado durante a inicialização com o comando ```sudo systemctl enable blink_python```.


## 📌 Resultados

A seguir, encontra-se uma foto do circuito desenvolvido:

<div align="center">
<img width='600px' src="https://imgur.com/ycmunIn.png"/>
</div>

No gif abaixo pode também ser visualizado o funcionamento dos serviços durante a inicialização do sistema operacional. O LED branco está conectado a porta ```GPIO 18``` e, portanto, é ligado pelo serviço escrito em ```bash```, enquanto o LED vermelho está conectado a porta ```GPIO 23```, sendo ativado pelo serviço escrito em ```Python```.

![](https://github.com/rafaeldschultz/sel0630-praticas/blob/main/pratica6/blinking_led.gif)

O funcionamento completo pode ser visualizado em: https://drive.google.com/file/d/1s54LQpRmTbP7kyr3FTEZAI1r-usPO5f3/view?usp=sharing

## 👥 Autores

* **Rafael Dalonso Schultz** - 11800945
* **Ana Julia Aguiar Tagliassachi** - 11800632

Construído com base nos códigos disponibilizados pelo professor Pedro Oliveira, do Departamento de Engenharia Elétrica de São Carlos e nos tutoriais disponibilizados pelas bibliotecas utilizadas.
