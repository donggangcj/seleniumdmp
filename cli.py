#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : cli.py
@Author: donggangcj
@Date  : 2018/11/16
@Desc  : 
'''
"""
Command Line Tool
"""
import argparse

from autoaddapi import autoaddjob

parser = argparse.ArgumentParser()
parser.add_argument("path", help="the date path need import ")
parser.add_argument('time', type=int, help='The sleep time,according to the net')
args = parser.parse_args()
autoaddjob(args.path, args.time)
