"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

from distutils.log import error
from genericpath import exists
import arrow
import nose    # Testing framework
from acp_times import open_time, close_time
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_zero_distance():
    inputTime = arrow.get("2022-02-03T20:27")
    outputTime = arrow.get("2022-02-03T20:27")
    assert outputTime == open_time(0, 1000, inputTime)

def test_negative_distance():
    inputTime = arrow.get("2022-02-03T20:27")
    outputTime = arrow.get("2022-02-03T20:27")
    assert outputTime == open_time(-100, 1000, inputTime)

def test_negative_total_distance_open_time():
    inputTime = arrow.get("2022-02-03T20:27")
    try:
        temp = open_time(100, -20, inputTime)
    except:
        print("passing a negative distance for the total failed")

def test_too_long_total_distance_open_time():
    inputTime = arrow.get("2022-02-03T20:27")