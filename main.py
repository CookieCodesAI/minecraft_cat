from machine import Pin, PWM
import time

touch = Pin(34, Pin.IN)
servo = PWM(Pin(25), freq=50)

def servo_angle(degrees):
    degrees = max(0, min(180, degrees))
    pulse_us = 1000 + (degrees / 180) * 1000
    servo.duty_ns(int(pulse_us * 1000))

while True:

    while touch.value() == 0:
        time.sleep(0.01)
    print(touch.value())
    print("touched")

    for i in range(2):
        servo_angle(0)
        time.sleep(0.7)

        servo_angle(180)
        time.sleep(0.7)

    servo_angle(100)

    while touch.value() == 1:
        time.sleep(0.01)

    print("released")
    
    time.sleep(0.2)
