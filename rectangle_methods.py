from main import Interval
import numpy as np
from math import *

def left_rectangle(func: str, interval: Interval, step: float) -> float:
    '''Решение интеграла func на интервале interval с шагом step
    методом левых прямоугольников'''
    s = 0.0
    for x in np.arange(interval.left, interval.right, step):
        s = s + eval(func)
    s = s * step
    return s

def middle_rectangle(func: str, interval: Interval, step: float) -> float:
    '''Решение интеграла func на интервале interval с шагом step
    средних прямоугольников'''
    s = 0.0
    for x in np.arange(interval.left + step/2, interval.right, step):
        s = s + eval(func)
    s = s * step
    return s


def right_rectangle(func: str, interval: Interval, step: float) -> float:
    '''Решение интеграла func на интервале interval с шагом step
    правых прямоугольников'''
    s = 0.0
    for x in np.arange(interval.left+step, interval.right, step):
        s = s + eval(func)
    s = s * step
    return s
