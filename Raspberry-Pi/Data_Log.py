import time
import board
import busio
import digitalio
import adafruit_gps



led = digitalio.DigitalInOut(board.LED)     # sets up LED in these 2 lines
led.direction=digitalio.Direction.OUTPUT 

uart = busio.UART(board.GP4, board.GP5, baudrate=9600, timeout=10) #
gps = adafruit_gps.GPS(uart, debug=False) 


gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")


last_print = time.monotonic()
with open("/gps.txt", "a") as fp:
while True:

        gps.update()
        # Every second print out current location details if there's a fix.
        current = time.monotonic()
        if current - last_print >= 1.0:
            last_print = current
            if not gps.has_fix:
                # Try again if we don't have a fix yet.
                print("Waiting for fix...")
                time.sleep(.5)
                continue
            
            print(gps.latitude)
            print(gps.longitude)    

            fp.write(f'{gps.latitude}, {gps.longitude}\n')
            fp.flush()

            led.value = True
            time.sleep(1)
            led.value = False

           
   
        

