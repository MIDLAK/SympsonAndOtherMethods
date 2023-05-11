from dataclasses import dataclass
import numpy as np
from math import *


from rectangle_methods import *


@dataclass
class Interval:
    left: float
    right: float


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


def simpson(func: str, interval: Interval, step: float) -> float:
    s = 0.0
    i = 0 # счётчик
    for x in np.arange(interval.left, interval.right, step):
        if i%2 == 0:
            s = s + 4 * eval(func)
        else:
            s = s + 2 * eval(func)
        i = i + 1

    x = interval.left
    func_left_value = eval(func)
    x = interval.right
    func_right_value = eval(func)

    s = step/3 * (func_left_value + func_right_value + s)
    return s


def runge_condition(interval: Interval, eps: float, step: float, \
        order_acc: float, func_value: float, \
        func_value_less_step: float) -> bool:
    '''Условие Рунге для интервала interval с точностью eps, 
    шагом step и классом точности order_acc'''
    if eps*step/(interval.right - interval.left) >= \
            abs(func_value_less_step - func_value)/(2**order_acc-1):
        return True
    elif abs(func_value_less_step - func_value) <= eps:
        return True
    else:
        return False


def runge_auto_step(method_ptr, func: str, interval: Interval, \
        start_step: float, order_acc: float, eps=0.0001) -> tuple[float, float]:
    '''method_ptr - указатель на функцию.
    В качестве первого параметра возвращается значение интеграла,
    второго - количество проделанных уменьшений шага'''
    runge_flag = False
    steps_count = 0
    step = start_step

    # дробление шага до тех пор, пока не будет выполнено условие Рунге
    while True:
        func_value = method_ptr(func, interval, step)
        step = step / 2
        func_value_less_step = method_ptr(func, interval, step)
        runge_flag = runge_condition(interval, eps, step, order_acc, func_value,
                                     func_value_less_step)
        steps_count = steps_count + 1
        if runge_flag or steps_count > 10000:
            break
    return (func_value_less_step, steps_count)


def main():
    func = str(input('Функция>'))

    left = float(input('Нижняя граница интегрирования>'))
    right = float(input('Верхняя граница интегрирования>'))
    interval = Interval(left=left, right=right)

    amount_points = int(input('Количество отрезков>'))
    start_step = (right-left)/amount_points

    print(f'∫{func} от {interval.left} до {interval.right} равен:')
    print(f'метод левых прямоугольников: {left_rectangle(func=func, interval=interval, step=start_step)}')
    print(runge_auto_step(method_ptr=left_rectangle, func=func, interval=interval, order_acc=2, start_step=start_step))
    print(f'метод средних прямоугольников: {middle_rectangle(func=func, interval=interval, step=start_step)}')
    print(runge_auto_step(method_ptr=middle_rectangle, func=func, interval=interval, order_acc=2, start_step=start_step))
    print(f'метод правых прямоугольников: {right_rectangle(func=func, interval=interval, step=start_step)}')
    print(runge_auto_step(method_ptr=right_rectangle, func=func, interval=interval, order_acc=2, start_step=start_step))
    
    print(trapeze(func=func, interval=interval, step=start_step))
    print(runge_auto_step(method_ptr=trapeze, func=func, interval=interval, order_acc=4, start_step=start_step))

    print(simpson(func=func, interval=interval, step=start_step))
    print(runge_auto_step(method_ptr=simpson, func=func, interval=interval, order_acc=4, start_step=start_step))


if __name__ == '__main__':
    main()
