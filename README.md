# Autonomous-Robot-System

In order to recreate the system below you will need to build a DonKeyCar. 

DonkeyCar
---------
If you don't have one and would like to build one please visit: https://www.donkeycar.com/

This site contains all that is needed to re-build this system.

Below is a detailed diagram of all the components you will find within the DonkeyCar Application.

![image](https://user-images.githubusercontent.com/78712154/166343124-e58a7262-2364-4f95-889b-4d6475268db6.png)



Object Detection
----------------
The model below is googles coco object detector. It can detect up to 91 objects.

This model was integrated with DonkeyCar using python scripts.

Uses version ssd_mobilenet_v3_coco_2020, below i wrote a typo in the diagram it supposed to say through opencv not to.

![image](https://user-images.githubusercontent.com/78712154/166343112-4c0e437c-1813-440b-b385-46d4d3bcb3c4.png)



This System
-----------

This system integrates the two above systems. Within this repository you have all that is needed for object detection and automation.

It does this using python selenium.

All you need is a bot to intergrate into this system.

Run the main.py file after passing an object for it to  detect, then point it to a webserver/video stream of your bot.

Also point the selsscripts to the controls of your bot.

Current system is made to handle 1 object and two scripts, however can be scaled up to 8 objects and over 10 scripts depending on logic.

This architecture is not mainly dependant on opencv and python selenium DonkeyCar was an optional passion build for me.

![image](https://user-images.githubusercontent.com/78712154/166343070-e389e24b-729b-4a3f-aa74-6e0719ad4a8d.png)



