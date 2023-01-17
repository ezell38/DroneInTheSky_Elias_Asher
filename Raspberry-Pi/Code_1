from adafruit_ugpio import UGPDevice #import the ultimate gps module
import board
import time 
 
PPS_PIN = board.D1 # assign pin D1 on Raspberry Pi Pico as the Pulse Per Second (PPS) Pin for GPS Module 
gps = UGPDevice(PPS_PIN) #create an instance of UGPDevice using control from PPS pin 1. 
 
# continue only if a GPS device was found on the port specified above 
if gps.has_fix:

    # read longitude and latitude from GPS module into variables below  
    lat = gps.latitude 
    lon = gps.longitude

    # save current location to file for tracking or reference later  
    with open("locationlog.csv", "a") as log:  

        log.write("{}, {}\n".format(lon, lat))

        print("Location added to log.")