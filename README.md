# Drone_In_The_Sky

&nbsp;

## Table of Contents
* [Planning](#Planning)
* [Week 1-4](#Weeks_1-4)



## Planning

### Materials 

 - Cheerwing Drone - CW4
 
 - Rasberry Pi - 6 grams
 
 - [Ultimate GPS](https://learn.adafruit.com/adafruit-ultimate-gps/circuitpython-python-uart-usage) - 8.5 grams
 
 - Circuitboard - 10 grams
 
 - Wires 
 
 - Accelerometer 

 - Box to hold onboard pico
 
 - Laser cut/3D printed fastening pieces
 
 - IR Remote 

 - LiPo battery + Powerboost 500c Module - 14 grams
 
 - [LORA](https://www.adafruit.com/product/3072)
 
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


## Weeks_1-4

During these weeks we completed the planning document and slowly finalized/revised our project until we decided on what our first, reasonable iteration would be. We then completed the PseudoCode and CAD design for the project.

### PseudoCode

 - Initialize Ultimate GPS module

 - Connect Google maps to PC

 - Connect to Ultimate GPS to Pico

 - Track Projectile while being flown

 - Data is converted to positioning on map

 - Automate Drawing Lines between data points

 - Send images to mobile device

 - Print data 

### CAD 

For this assignment we needed to attach the GPS tracker onto a tello drone so we are able to attach it. We used a previous CAD design that was meant to hold an egg over a tello and then remodeled it to hold the circuitboard, Rasberry Pi PICO, battery, and Adafruit Ultimate GPS. A major blcok in this project was keeping the total mass of the required modules as well as the printed CAD attachment under the tello weight restriction of 60 grams. We ended up acheiving this by cutting slits in the CAD design to cut down the weight. 

<img src="images/Project_1.PNG" width="400" height="300" />

<img src="images/Project_2.PNG" width="400" height="300" /> 

<img src="images/Project_3.PNG" width="400" height="300" /> 


[CAD Link](https://cvilleschools.onshape.com/documents/748b0624d922708572d6db59/w/4d4ce83156b394ee96ab4f9d/e/5392185db1c275d61a384980)


