#!/usr/bin/env python

import time

import RPi.GPIO as GPIO

from rele import rele

admin_rele = rele(GPIO)

admin_rele.set_on(1)
admin_rele.set_off(1)
admin_rele.set_on(0.5)
admin_rele.set_off(0.5)
for i in range(1,7*3+1):
    admin_rele.set_on(0.1)
    admin_rele.set_off(0.1)
    admin_rele.set_on(0.1)
    admin_rele.set_off(0.1)
    admin_rele.set_on(0.2)
    admin_rele.set_off(0.2)
    if i % 7 == 0:
        admin_rele.set_on(0.05)
        admin_rele.set_off(0.05)
        admin_rele.set_on(0.05)
        admin_rele.set_off(0.05)
        admin_rele.set_on(0.05)
        admin_rele.set_off(0.05)
        admin_rele.set_on(0.05)
        admin_rele.set_off(0.05)
        admin_rele.set_on(0.2)
        admin_rele.set_off(0.2)
        
    

GPIO.cleanup()