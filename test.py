import machine
from time import sleep as pause 

led = machine.Pin("LED", machine.Pin.OUT)

while 1:
    led.toggle()
    pause(1)
    