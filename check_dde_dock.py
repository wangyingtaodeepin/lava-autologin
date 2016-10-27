#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil
import sys
import time

def isTaskExist(name):
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == name:
            print("Task %s exist." % name)
            return True
    return False

timeout = 180

while True:
    if isTaskExist("dde-dock"):
        time.sleep(30)
        sys.exit(0)
    elif timeout != 0:
        time.sleep(1)
        timeout = timeout - 1
        print(timeout)
        continue
    else:
        sys.exit(1)

