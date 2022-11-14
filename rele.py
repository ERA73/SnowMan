#!/usr/bin/env python

import time
import traceback

import RPi.GPIO as GPIO

class rele:
	def __init__(self):
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
	
	def switch(self, flag, sec = 0.1):
		if flag:
			self.set_on(sec)
		else:
			self.set_off(sec)

	def close(self):
		GPIO.cleanup()