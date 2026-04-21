from machine import Pin, PWM
from utime import sleep_ms

#----KONSTANTY A NASTAVENÍ----
MAX_JAS = 65535  #Max hodnota pro PWM 100% svítí
MIN_JAS = 0      #Min hodnota pro PWM 0% svítí
FREKVENCE = 1000 #Kolikrát za vteřinu se stihne rozsvítít 

#----Inicializace (vše PWM)----
leds = []

for i in range(4):
    p = PWM(Pin(i))
    p.freq(FREKVENCE)
    p.duty_u16(MIN_JAS)
    leds.append(p)

#----Wrappery (pomocné funkce)----
def zapni(led):
    led.duty_u16(MAX_JAS)

#---MAIN část----
while True:
    try:
        zapni(leds[0])
    except KeyboardInterrupt:
        break