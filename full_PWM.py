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

def vypni(led):
    led.duty_u16(MIN_JAS)

def zhasni_vse():
    for led in leds:
        vypni(led)

def zapni_pozvolna(led):
        for duty in range(MIN_JAS, MAX_JAS, 1500):
            led.duty_u16(duty)
            sleep_ms(20)   

def vypni_pozvolna(led):
        for duty in range(MAX_JAS, MIN_JAS, -1500):
            led.duty_u16(duty)
            sleep_ms(20)
        led.duty_u16(0)


#----PWM Animace----
def PWM_RIGHT_ON():
    zhasni_vse()
    for led in leds:
        zapni_pozvolna(led)

def PWM_RIGHT_OFF():
    for led in leds:
        vypni_pozvolna(led)

def PWM_LEFT_ON():
    zhasni_vse()
    for led in reversed(leds):
        zapni_pozvolna(led)

def PWM_LEFT_OFF():
    for led in reversed(leds):
        vypni_pozvolna(led)

def BREATH_ON():
    zhasni_vse()
    for duty in range(MIN_JAS, MAX_JAS, 1500):
        for led in leds:
            led.duty_u16(duty)
        sleep_ms(20)

def BREATH_OFF():
    zhasni_vse()
    for duty in range(MAX_JAS, MIN_JAS, -1500):
        for led in leds:
            led.duty_u16(duty)
        sleep_ms(20)
        led.duty_u16(0)
#----Animace----
def hadR():
    zhasni_vse()
    for led in leds:
        zapni(led)
        sleep_ms(200)
        vypni(led)

def hadL():
    zhasni_vse()
    for led in reversed(leds):
        zapni(led)
        sleep_ms(200)
        vypni(led)

def leftRight():
    hadR()
    hadL()

def blik():
    zhasni_vse()
    sleep_ms(50)
    for led in leds:
        zapni(led)
    sleep_ms(50)

def blikOb():
    zhasni_vse()
    for j in range(2):
        for i, led in enumerate(leds):
            if i % 2 == 0:
                zapni(led)
        sleep_ms(100)
        zhasni_vse()
        sleep_ms(100)

    for j in range(2):
        for i, led in enumerate(leds):
            if i % 2 != 0:
                zapni(led)
        sleep_ms(100)
        zhasni_vse()
        sleep_ms(100)

#---MAIN část----
while True:
    try:
        BREATH_ON()
        BREATH_OFF()
        #PWM_LEFT_ON()
        #PWM_LEFT_OFF()
        #PWM_RIGHT_ON()
        #PWM_RIGHT_OFF()
        #zapni_pozvolna(leds[0])
        #vypni_pozvolna(leds[0])
        #blikOb()
        #blik()
        #leftRight()
        #hadL()
        #hadR()
        #vypni(leds[0])
        #zapni(leds[0])
    except KeyboardInterrupt:
        zhasni_vse()
        break
