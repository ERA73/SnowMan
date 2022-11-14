#!/usr/bin/env python

import time

from rele import rele
from sound_scanner import sound_scanner

admin_rele = rele()

"""
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
admin_rele.close()
"""



admin_relay = rele()

admin_scanner = sound_scanner(admin_relay.switch, 7)
admin_scanner.start()
admin_scanner.close()