import network
import socket
from time import sleep
from umachine import *
import time

led = Pin("LED", Pin.OUT)
led.toggle()


ssid = '2WIRE141'
password = '0200371906'
print('ssid and password set')
    
def connect():
#Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
#     address = (ip, 80)
#     connection = socket.socket()
#     connection.bind(address)
#     connection.listen(1)
#     print(connection)
    #return connection

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp socket
    server_address = (ip, 10000)
    print ('Server starting up on %s port %s' % server_address)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    
    while True:
# Wait for a connection
        print ('Server waiting for a connection...')
        connection, client_address = sock.accept()
        try:
            print ('Server connection from', client_address)
# Receive the data in small chunks and process it
            while True:
                data = connection.recv(16)
                print ('Server received "%s"' % data)
                print('done1')
                secs = time.time()
                secs = get_temp()
                connection.send(str(secs))
                print('done2')
                print(secs)
                if data:
                    string = data.decode('ascii')
                    if string == '12345':
                        led.toggle() #toggle onboard LED if correct data received
                #else:
                    #print ('no more data from', client_address)
                    #break
        finally:
            connection.close()
        
def get_temp():
    sensor_temp = machine.ADC(4)
    cf = 3.3/65535
    temp = sensor_temp.read_u16() * cf
    temC = 27 - ( temp - 0.706 )/ 0.001721
    temF = temC * 9/5 + 32
    return temF


try:
    ip = connect()
    connection = open_socket(ip)
    print('done3')
except KeyboardInterrupt:
    machine.reset()











