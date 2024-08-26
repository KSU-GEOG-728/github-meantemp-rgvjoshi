#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: mean_temp.py
    Author: Raghav Joshi
    Description:  Calculates mean daily temperature from two user defined variables representing a daily high (x) and low (y) temperature
    Date created: 08/26/2024
    Python Version: 3.9.16
"""

# Assign variable x the value for the previous day's high temperature
x = 103.5

# Assign variable y the value for the previous day's low temperature
y =  79.2

# Create variable z and use mathematical operators to calculate the mean temperature
z = (x+y)/2

# Use this custom statement that prints the result to screen
print("Yesterday's mean daily temperature was {0} degrees.".format(z))
