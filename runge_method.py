from Interval import Interval

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

