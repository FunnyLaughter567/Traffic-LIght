from gpiozero import LED, Button
from time import sleep
import random

count = 0
button1 = Button(17)
greenled = LED(4)
redled = LED(23)
yellowled = LED(15)

while(count < 5):
    redled.off()
    yellowled.off()
    greenled.on()
    sleep(6)
    greenled.off()
    yellowled.on()
    sleep(3)
    yellowled.off()
    redled.on()
    sleep(6)
    count += 1
      
greenled.off()
redled.off()
yellowled.off()