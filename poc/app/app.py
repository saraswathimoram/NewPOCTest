#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Checing Codecoverage, pyling, unitest
"""

def add(arg1, arg2):
    """ function will add two values"""
    return arg1+arg2

k = 0

def subtract(arg1, arg2):
    """ function will subtract two params"""
    return arg1-arg2

def multiply(arg1, arg2):
    """ function will multiply two params"""
    return arg1*arg2

def devide(arg1, arg2):
    """ function will devide two params"""
    if arg2 == 0:
        raise ValueError("Not devisable by zero")
    return arg1/arg2

#pylint app.py
