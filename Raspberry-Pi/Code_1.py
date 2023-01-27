import time
import board
import busio 
import adafruit_gps

# create the I2C interface connection to the GPS module 
UART = busio.UART(board.TX, board.RX, baudrate=9600) 
gps = adafruit_gps.GPS(UART)  # Use UART for connection 
# Initialize GPS module by setting update rate to once a second  
gps.send_command(b"PMTK220,1000")   # Set update rate to once a second (1Hz) 
# Establish connection to Raspberry Pi Pico   
data_file = open("GPSdata.txt", "w")   # Open file in write mode (overwrites existing data)  

 while True:  # Main loop - keep going forever   

     gps.update()                    # Update GPS module readings  

     if gps.has_fix:     # Verify that there are signal datas            

         lat, lon = gps.latitude, gps.longitude    # Save lat and long data     

         data_file.write("{0},{1}\n".format(lat, lon))    # Append new data as lat and long into text file      

     time.sleep(1)                   # Pause for 1 second between each loop iteration 

 data_file.close()                  # When main loop completes, close the text file