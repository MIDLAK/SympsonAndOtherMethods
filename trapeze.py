import numpy as np
from Interval import Interval
from math import *

def trapeze(func: str, interval: Interval, step: float) -> float:
    '''Решение интеграла func на интервале interval с шагом step
    методом трапеции'''
    s = 0.0
    for x in np.arange(interval.left+step, interval.right, step):
        s = s + eval(func)

    x = interval.left
    func_left_value = eval(func)
    x = interval.right
    func_right_value = eval(func)

    s = step * (s + (func_left_value + func_right_value) / 2)
    return s
