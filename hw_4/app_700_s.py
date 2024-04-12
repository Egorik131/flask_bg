'''Задание №7
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.'''

'''Синхронно'''

import time
from random import randint

my_arr = [randint(1, 100) for i in range(1_000_000_00)]
start_time = time.time()


def summ_elements(arr):
    summ_elem = 0
    for i in range(len(arr)):
        summ_elem += arr[i]
    print(f'Сумма элементов массива: {summ_elem:_}. Время выполнения: {time.time() - start_time:.2f} сек.')


summ_elements(my_arr)