#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on July 23 2020 @ HongKong
Author: Changlong Li
Email: liclong@mail.ustc.edu.cn
"""

# ps -le | grep "com.sina.news"
import os
import subprocess
import time

file_name = '../workload/activity_name.xml'


def xml_analyzer(file_name):
    f = open(file_name, 'r')
    activity_list = list(f)
    f.close()
    return activity_list


if __name__ == '__main__':
    activity_list = xml_analyzer(file_name)
    for activity_name in activity_list:
        print(activity_name)
        f = os.popen('adb shell am start -W ' + activity_name, 'r')
        output = f.read()
        #print(output)
        package_name = output.split('cmp=')[1].split(' ')[0].split('/')[0]
        #print('package name is: ' + package_name)
        f.close()
        time.sleep(1)
        # f = os.popen('adb shell top -n 1 | grep "news"', 'r')
        f = os.popen('adb shell ps -le | grep news > process.txt', 'r')
        output2 = f.read()
        print(output2)
        f.close()

        print('Input enter for the next app ...')
        input()