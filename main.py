import numpy as np
from math import *

from rectangle_methods import *
from runge_method import *
from Interval import Interval
from trapeze import *
from simpson import *


def main():
    func = str(input('Функция>'))

    left = float(input('Нижняя граница интегрирования>'))
    right = float(input('Верхняя граница интегрирования>'))
    interval = Interval(left=left, right=right)

    amount_points = int(input('Количество отрезков>'))
    start_step = (right-left)/amount_points

    eps = float(input('Погрешность для метода Рунге>'))

    print(f'∫{func} от {interval.left} до {interval.right} равен:')

    # методы прямоугольников
    print(f'метод левых прямоугольников: {left_rectangle(func=func, interval=interval, step=start_step)}')
    print(runge_auto_step(method_ptr=left_rectangle,\
            func=func, interval=interval, order_acc=2, start_step=start_step, eps=eps))
    print(f'метод средних прямоугольников: {middle_rectangle(func=func, interval=interval, step=start_step)}')
    print(runge_auto_step(method_ptr=middle_rectangle,\
            func=func, interval=interval, order_acc=2, start_step=start_step, eps=eps))
    print(f'метод правых прямоугольников: {right_rectangle(func=func, interval=interval, step=start_step)}')
    print(runge_auto_step(method_ptr=right_rectangle,\
            func=func, interval=interval, order_acc=2, start_step=start_step, eps=eps))
    
    # метод трапеции
    print(f'метод трапеции: {trapeze(func=func, interval=interval, step=start_step)}')
    print(runge_auto_step(method_ptr=trapeze,\
            func=func, interval=interval, order_acc=4, start_step=start_step, eps=eps))

    # метод Симпсона
    print(f'метод Симпсона: {simpson(func=func, interval=interval, step=start_step)}')
    print(runge_auto_step(method_ptr=simpson,\
            func=func, interval=interval, order_acc=4, start_step=start_step, eps=eps))

    print('Примечание: в скобках указывается значение, найденное с автоматическим шагом и количество шагов на достижение условия Руге')


if __name__ == '__main__':
    main()
