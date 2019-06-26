#14 is buzzer
#22 is PIR

from gpiozero import Buzzer, MotionSensor   #imports necessary gpiozero tools
from time import sleep  #imports sleep


alarm = Buzzer(14)  #shortens the syntax for Buzzer
sensor = MotionSensor(23)   #shortens syntax for MotionSensor

while True: #infinite loop
    if sensor.motion_detected:  #checks for motion
        alarm.on()  #turns alarm on
        sleep(.5)   #waits .5 seconds
        alarm.off() #turns alarm off
        sleep(.25)  #waits .25 seconds
