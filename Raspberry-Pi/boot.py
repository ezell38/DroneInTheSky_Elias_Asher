import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.GP15)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

if not switch.value:
    storage.remount("/", readonly=False)


# with open("/tmp.txt", "a") as fp:
# fp.write(switch.value)

#if stuck!!!!! use this below in the terminal:
    # import os
    # os.listdir("/")
    # os.rename("/boot.py", "/boot.bak")