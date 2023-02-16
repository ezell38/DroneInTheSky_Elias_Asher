import time
import board
import busio
import digitalio
import adafruit_gps



led = digitalio.DigitalInOut(board.LED)     # sets up LED in these 2 lines
led.direction=digitalio.Direction.OUTPUT 

uart = busio.UART(board.GP4, board.GP5, baudrate=9600, timeout=10)

gps = adafruit_gps.GPS(uart, debug=False) 

gps.latitude=lat
gps.longitude=lon

while.True:
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
       if current - last_print >= 1.0:
        last_print = current

    if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            led.value = False
            continue




    with open("/gps.txt", "a") as fp:
        while True:
            temp = microcontroller.cpu.temperature
            # do the C-to-F conversion here if you would like
            fp.write(f'{lat}, {lon}\n'.format(gps.latitude))
            fp.flush()
            led.value = not led.value
            time.sleep(1)
