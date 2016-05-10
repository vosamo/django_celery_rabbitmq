#!/usr/bin/env python
# coding=utf-8
import time
import commands
from celery.task import task
@task
def ground_work():
    time_cmd = "ntpdate time.nist.gov"
    print "------TASK BEGIN------" 
    time.sleep(10)                      # Simulate time-consuming operation with sleep.
    res = commands.getoutput(time_cmd)
    print '------TASK END------'
    return res

if __name__ == '__main__':
    ground_work('test1')
