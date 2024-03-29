
import time
import board
import busio
import digitalio
import adafruit_gps

led = digitalio.DigitalInOut(board.LED)     # sets up LED in these 2 lines
led.direction=digitalio.Direction.OUTPUT 

uart = busio.UART(board.GP4, board.GP5, baudrate=9600, timeout=10) #
gps = adafruit_gps.GPS(uart, debug=False) 

prev_lat = 0.0
prev_long = 0.0


gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,500")


with open("/NEWWORKTEST2.txt", "a") as textFile:
    while True:
        update = gps.update()
        # Every second print out current location details if there's a fix.

        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            time.sleep(.5)
            continue

        else:
            latitude = round(float(gps.latitude), 4)
            longitude = round(float(gps.longitude), 4)

            if update and not ((prev_lat == latitude) and (prev_long == longitude)):

                print(latitude)
                print(longitude)
                print(gps.timestamp_utc.tm_min)
                print(gps.timestamp_utc.tm_sec)
                print("-" * 40) 
                
                textFile.write(f'{latitude}, {longitude}\n')
                textFile.flush()
                    
                prev_lat = latitude
                prev_long = longitude

                led.value = True
                time.sleep(1)
                led.value = False
            else:
                print("-No new values-")

