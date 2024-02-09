# Complete Project Details: https://RandomNerdTutorials.com/raspberry-pi-detect-motion-pir-python/

from gpiozero import MotionSensor
from signal import pause
import time

pir = MotionSensor(4)
print("Finished wiring...")

#while True:
#    pir.wait_for_motion()
#    if pir.motion_detected:
#        print("Motion detected")
#        time.sleep(2)

def motion_function():
    print("Motion Detected")

def no_motion_function():
    print("Motion stopped")

pir.when_motion = motion_function
pir.when_no_motion = no_motion_function

pause()
