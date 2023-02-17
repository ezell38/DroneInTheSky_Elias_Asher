import board
import storage
import math
import busio
import digitalio
import adafruit_gps
import time

[x1, y1] = input("Enter coordinate 1: ").split(",")                 #takes an input of 2 variables using the split method
[x2, y2] = input("Enter coordinate 2: ").split(",")
[x3, y3] = input("Enter coordinate 3: ").split(",")

data = [[x1, y1], [x2, y2], [x3, y3]]

with open("/testVars.txt", "a") as fp:
    for i in range(len(data)):
        fp.write(f'{data[i][0]}, {data[i][1]}\n')
        fp.flush()
        led.value = not led.value
        time.sleep(1)


