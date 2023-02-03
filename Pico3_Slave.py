#Import the necessary files and libraries
from machine import Pin, SPI

#initialize the SPI bus
spi = SPI(1, baudrate= 1000000, polarity = 0, phase=0)

#initialize the onboard LED and the slave select pin.
LED = Pin('LED', Pin.OUT)
slave1_select = Pin(16, Pin.IN)

while True:
    #wait for the slave select line to be asserted by the master device
    while slave1_select.value() == 1:
        pass
    #read data from the SPI bus and decode it from binary to a string
    data = spi.read(1) #read 1 byte of data
    #data = data.decode()
    print (data)
    
    #check the received data
    if data == b'1':
        print("Received data: 1, Turning On LED")
        led.value(1)
        
    elif data == b'2':
        print("Received data: 2, Turning OFF LED")
        led.value(0)
        
    else:
        print("Invalid data received!!")
    
