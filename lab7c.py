#!/usr/bin/env python3
# Student ID: mvaseghi1
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        extra_minutes = sum.second // 60  # Integer division for minutes to carry
        sum.second = sum.second % 60     # Remainder becomes new seconds
        sum.minute += extra_minutes      # Add carried minutes
    
    # Handle minutes overflow
    if sum.minute >= 60:
        extra_hours = sum.minute // 60   # Integer division for hours to carry
        sum.minute = sum.minute % 60     # Remainder becomes new minutes
        sum.hour += extra_hours          # Add carried hours
    return sum

def change_time(time, seconds):
    total_seconds = time.hour * 3600 + time.minute * 60 + time.second + seconds
    if total_seconds < 0:
        total_seconds = 0  # or could wrap around
        
    time.hour = total_seconds // 3600
    total_seconds %= 3600
    time.minute = total_seconds // 60
    time.second = total_seconds % 60
    return None

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from midnight'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time