#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on July 23 2020 @ HongKong
Author: Changlong Li
Email: liclong@mail.ustc.edu.cn
"""

import os
import random
import time
from xlsxwriter import Workbook

file_name = 'activity_name.xml'

activity_list = []


def xml_analyzer(file_name):
    f = open(file_name, 'r')
    activity_list = list(f)
    f.close()
    return activity_list


def manual_launch():
    print('================ Launch apps manually ================')
    activity_list = xml_analyzer(file_name)
    wait_time = {}
    for activity_name in activity_list:
        print(activity_name)
        f = os.popen('adb shell am start -W ' + activity_name, 'r')
        output = f.read()
        print(output)
        package_name = output.split('cmp=')[1].split(' ')[0]
        latency = int(output.split('WaitTime: ')[1].split('\n')[0])
        wait_time[package_name] = latency
        f.close()
        print('Input enter for the next app ...')
        input()
    return wait_time


def auto_launch(activity_list):
    print('================ Launch apps automatically ================')
    wait_time = {}
    for activity_name in activity_list:
        print(activity_name)
        f = os.popen('adb shell am start -W ' + activity_name, 'r')
        output = f.read()
        #print(output)
        #package_name = output.split('cmp=')[1].split(' ')[0]
        #latency = int(output.split('WaitTime: ')[1].split('\n')[0])
        #wait_time[package_name] = latency
        f.close()
        #print('Input enter for the next app ...')
        time.sleep(30)
    return wait_time


def time_record():
    players = [{'dailyWinners': 3, 'dailyFree': 2, 'user': 'Player1', 'bank': 0.06},
               {'dailyWinners': 3, 'dailyFree': 2, 'user': 'Player2', 'bank': 4.0},
               {'dailyWinners': 1, 'dailyFree': 2, 'user': 'Player3', 'bank': 3.1},
               {'dailyWinners': 3, 'dailyFree': 2, 'user': 'Player4', 'bank': 0.32}]

    ordered_list = ["user", "dailyWinners", "dailyFree",
                    "bank"]  # list object calls by index but dict object calls items randomly

    wb = Workbook("launch_time.xlsx")
    ws = wb.add_worksheet("launch_time_statistic")  # or leave it blank, default name is "Sheet 1"

    first_row = 0
    for header in ordered_list:
        col = ordered_list.index(header)  # we are keeping order.
        ws.write(first_row, col, header)  # we have written first row which is the header of worksheet also.

    row = 1
    for player in players:
        for _key, _value in player.items():
            col = ordered_list.index(_key)
            ws.write(row, col, _value)
        row += 1  # enter the next row
    wb.close()


if __name__ == '__main__':
    # wait_time = manual_launch()
    activity_list = xml_analyzer(file_name)
    for i in range(8):
        wait_time = auto_launch(activity_list)
        random.shuffle(activity_list)
    # TODO: run auto_launch() for ten rounds, and output the results as an excel together
    # time_record()