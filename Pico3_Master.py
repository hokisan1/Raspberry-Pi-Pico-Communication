#import the necessary files and libraries
from machine import Pin, SPI
from time import sleep

#Initialize the SPI bust on the master device
spi = SPI(1, baudrate = 1000000, polarity = 1, phase = 1)
#the MOSI, MISO and SCK pins are automatically initialized by the SPI() constructor
# by using instance spi = SPI(1) it uses SPI bus 1 in our case MOSI(19), MISO(18), SCK(23)

#initialize the slave select pins for the two devices
slave1_select = Pin(16, Pin.OUT)
slave2_select = Pin(17, Pin.OUT)

#Request input from the user
slave_id = input("Enter the slave device id to communicate with (1 or 2): ")
#convert the input to an integer
slave_id = int(slave_id)
#Enter the data to send (1 is On and 2 is OFF)
data = input("Enter the data to send to slave: ")
while True:
    #based on the input choose the device to communicate with
    if slave_id == 1:
        slave1_select.value(0)
        slave2_select.value(1)
        print (slave_id)
    
        spi.write(data.encode())
        print (data.encode()) #Prints the data we have encoded in binary
        sleep(0.01)
        
    elif slave_id == 2:
        slave1_select.value(1)
        slave2_select.value(0)
        
        spi.write(data.encode())
        #print (data.encode()) #Prints the data we have encoded in binary
        sleep(0.01)
        
    else:
        print("Invalid input, Please enter option 1 or 2")
        
