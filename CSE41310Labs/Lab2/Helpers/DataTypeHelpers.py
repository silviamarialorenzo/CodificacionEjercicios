# Lab 2 - Part 1 - Silvia Maria Lorenzo

__all__ = ['isInt', 'isFloat', 'isDate']

from datetime import datetime

# This function accepts a string value and returns True
# if that value can be parsed to an int data type, False otherwise.
def isInt(value):
    try:
        value = value.lstrip("+-")
        for i in range(len(value)):
            if value[i].isnumeric() != True:
                return False
            else:
                return True   
    except:
        return False


# This function accepts a string value and returns True if
# that value can be parsed to a float data type, False otherwise.
def isFloat(value):
    try:
        num = float(value)
        return True
    except:
        return False


# Extra Credit: This function accepts a string value and returns True if
# that value can be parsed to a date-time data type, False otherwise.
def isDate(value):
    try:
        date = datetime.fromisoformat(value)
        return True
    except:
        return False

