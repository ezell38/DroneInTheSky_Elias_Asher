import board
import storage
import digitalio
import time

[x1, y1] = input("Enter coordinate 1: ").split(",")                 # Takes an input of 2 integers using the split method
[x2, y2] = input("Enter coordinate 2: ").split(",")
[x3, y3] = input("Enter coordinate 3: ").split(",")

data = [[x1, y1], [x2, y2], [x3, y3]]                               # Arranges the data on a list

with open("/testVars.txt", "a") as fp:                              # Opens a new text file on the pico titled "testVars"
    for i in range(len(data)):                                      # Loops through the data
        fp.write(f'{data[i][0]}, {data[i][1]}\n')                   # and writes each data point onto the file
        fp.flush()
        led.value = not led.value                                   # Turns the onboard led to the opposite state
