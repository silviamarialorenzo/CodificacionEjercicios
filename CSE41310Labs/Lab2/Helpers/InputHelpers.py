# Lab 2 - Part 2 - Silvia Maria Lorenzo

from Helpers.DataTypeHelpers import *
from datetime import datetime

__all__ = ['inputInt', 'inputFloat', 'inputString', 'inputDate']


def inputInt(prompt="Enter an integer: ", min_value=0, max_value=100):
    while True:
        value = input(prompt)
        if isInt(value) is False:
            print("Value must be an integer")
            continue
        else:
            if int(value) < min_value or int(value) > max_value:
                print(f"Value must be between {min_value} and {max_value}")
                continue
            return int(value)


def inputFloat(prompt="Enter a float value: ", min_value=0, max_value=100):
    while True:
        value = input(prompt)
        if isFloat(value) is False:
            print("Value must be in the float format")
            continue
        else:
            if float(value) < min_value or float(value) > max_value:
                print(f"Value must be between {min_value} and {max_value}")
                continue
            return float(value)


def inputString(prompt="Enter a string: ", min_length=0, max_length=100):
    while True:
        string = input(prompt)
        if len(string) < min_length or len(string) > max_length:
            print(f"Text must be between {min_length} and {max_length} in length")
            continue
        return string


def inputDate(prompt="Enter a date in ISO format (yyyy-mm-dd): "):
    while True:
        value = input(prompt)
        if isDate(value) is False:
            print("Date must be in ISO format (yyyy-mm-dd)")
            continue
        else:
            return datetime.fromisoformat(value)
