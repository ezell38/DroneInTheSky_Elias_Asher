# Drone_In_The_Sky

&nbsp;

## Table of Contents
* [Planning](#Planning)



## Planning

### Materials 

 - Cheerwing Drone - CW4
 
 - Rasberry Pi
 
 - [Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-python-uart-usage) 
 
 - Breadboard
 
 - Wires 
 
 - Accelerometer 

 - Box to hold onboard pico
 
 - Laser cut/3D printed fastening pieces
 
 - IR Remote 

 - Battery
 
 - Battery Holder
 
 - LORA
 
### Images 

<img src="images/DITS_Drawing_1.PNG" width="400" height="300" /> <img src="images/PlanningImage_2.JPG" width="400" height="300" /> 

### Primary goal then following iterations 

Primary Goal - 

Use GPS with the L76B and a Pico to track a drone and display its path on a live map. 
Iterations - 

 - Make it send data in real time

 - Make a drone

 - Adding the button to turn the tracker on and off. Have a IR remote attached to the drone remote that controls when the PICO is drawing on the phone screen and when it isn't

Risk Mitigation - 

 - Hit someone with projectile/drone
 
 - Lose the GPS tracker if it doesn't work
  
 - Propeller blades can cause harm 
 
 - Muscular injury from walking to get drone or other projectile

Avoidance - 

We will wear safety glasses while flying the drone and doing other various tasks that could endanger our eyes. Properly warm-up before retrieving drone/projectile. 

### What we need to learn

 - How to add bluetooth to a pico
 
 - How to track distance using a pico 

 - How to map out a path on the screen from data
 

### Schedule

Weeks 1 and 2: We will complete the planning document besides code and cad sketches, schedule, and get permission. </br>
Week 3: We will complete pseudocode and CAD sketches of each part, and purchase/collect supplies. </br>
Weeks 4 and 5: We will start drafting the real code and CAD for printing, as well as wiring. </br>
Week 6: Complete process of connecting Pico to phone application and figure out display method. </br>
Week 7: Combine all components into full project for testing. </br>
Week 8: First Prototype test of flight, just tracking location and mapping. </br>
Week 9 and 10: Fix issues with code/flight. </br>
Week 11: Retest with new changes. </br>
Week 12: Implement new functions and test. </br>
Week 13 and 14: Finalize documentation and design.

### PseudoCode

 - Initialize Ultimate GPS module

 - Connect Google maps to PC

 - Connect to Ultimate GPS to Pico

 - Track Projectile while being flown

 - Data is converted to positioning on map

 - Automate Drawing Lines between data points

 - Send images to mobile device

 - Print data 
