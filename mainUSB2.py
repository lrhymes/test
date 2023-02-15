from time import sleep
from umachine import *
import time
import struct
import sys

led = Pin("LED", Pin.OUT)
led.toggle()
a0 = ADC(0)

# def get_temp():
#     sensor_temp = ADC(0) ##ADC(ADC.CORE_TEMP)
#     cf = 3.3/65535.0
#     temp = sensor_temp.read_u16()# * cf
#    #temp = float(t)
#    # temC = 27.0 - ( temp - 0.706 )/ 0.001721
#    # temF = temC * 9.0/5.0 + 32.0
#     return temp



#while True:
#    Temp = get_temp()
#    print(Temp)

# Temp = get_temp()
# print('%.30f' % Temp)
# baTemp = struct.pack("!f", Temp)
# 
# print(baTemp)
# print(list(baTemp))
# 
# TempUn = struct.unpack('>f', baTemp)[0]
# print('%.30f' % TempUn)


while True:
    #Temp = get_temp()
    Temp = a0.read_u16()
    baTemp = struct.pack("!I", Temp)
    sys.stdout.write(baTemp)
    led.toggle()
   # time.sleep(0.05)
    