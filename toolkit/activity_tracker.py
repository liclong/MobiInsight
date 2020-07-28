#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on July 22 2020 @ HongKong
Author: Changlong Li
Email: liclong@mail.ustc.edu.cn
"""


import os
import subprocess
import time
from tqdm import tqdm


"""
============================================================================

How to use this file to track the activity name of each app?
Three steps as follows:
1. Run this activity_tracker.
2. Launch the target app manually.
3. open the logcat.txt, then you will find the activity name from that file.

============================================================================
"""


def logcat_clean(logcat):
    if os.path.exists(logcat):
        os.system('rm ' + logcat)
    os.system('adb logcat -c')


if __name__ == '__main__':
    print('====================== App Activity Tracker ======================')
    if not os.path.exists('tmp'):
        os.system('mkdir tmp')
    logcat_clean('tmp/logcat.txt')
    time.sleep(0.5)
    print('Please launch the app you want to track ...')
    p = subprocess.Popen('adb logcat | grep "activity" > tmp/logcat.txt', shell=True)
    for i in tqdm(range(10)):
        time.sleep(1)
    p.kill()
    print('Please open \033[7;37;40mlogcat.txt\033[0m to track the activity name')
