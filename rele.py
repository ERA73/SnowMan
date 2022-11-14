#!/usr/bin/env python

import time
import traceback

class rele:
    def __init__(self, GPIO):
        self.controller = GPIO
        self.controller.setmode(self.controller.BCM)
        self.controller.setup(27, self.controller.OUT)
    
    def set_on(self, long = 1):
        try:
            self.controller.output(27, self.controller.LOW)
            time.sleep(long)
        except:
            traceback.print_exc()
    
    def set_off(self, long = 1):
        try:
            self.controller.output(27, self.controller.HIGH)
            time.sleep(long)
        except:
            traceback.print_exc()