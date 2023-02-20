# from umachine import Pin, PWM
# from time import sleep
# 
# led = PWM(Pin(15))
# led.freq(1000)
#  
# while True:
#     duty = int(pow(2,16)/2)
#     led.duty_u16(duty)
#
from umachine import Pin, PWM, ADC
import struct
import sys
import time
import array

a0 = ADC(0)
led = Pin(25,Pin.OUT)
led.toggle()

pout = Pin(15)
pwm15 = PWM(pout)
pwm15.freq(1000000)
pwm15.duty_u16(10000)

N = 256

Y = []
for i in range(0,N):
    Y.append(0)

while True:
    #Temp = get_temp()
    tick = sys.stdin.buffer.readline()
    #tick = sys.stdin.read(4)
    #f, = struct.unpack("<I", tick)
    f = int(tick)
    led.toggle()
    pwm15.freq(f)
    for i in range(0,N):
        Y[i] = a0.read_u16()
        #y = a0.read_u16()
    for i in range(0,N):
        t = struct.pack("<I", Y[i])
        sys.stdout.write(t)
#    time.sleep(0.1)
# led = umachine.Pin("LED", umachine.Pin.OUT)
# p15 = umachine.Pin(15, umachine.Pin.ALT_PWM)
# duty = int(pow(2,16)/2)
# p15.duty_u16(duty)
# p15.toggle(
    led.toggle()
