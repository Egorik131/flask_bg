'''Задание №7
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.'''

'''Многопроцессорность'''

import time
import multiprocessing
from random import randint

start_time = time.time()
my_arr = [randint(1, 100) for i in range(1_000_000)]
counter = multiprocessing.Value('i', 0)

def summ_elements(arr, cnt):
    for i in range(len(arr)):
        with cnt.get_lock():
            cnt.value += arr[i]
    print(f'Сумма элементов массива: {cnt.value:_}. Время выполнения: {time.time() - start_time:.2f} сек.')


if __name__ == '__main__':
    processes = []
    parts = 5
    piece_arr = len(my_arr) // parts
    for i in range(parts):
        p = multiprocessing.Process(target=summ_elements, args=(my_arr[piece_arr * i:piece_arr * (i + 1)], counter,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'Общее время выполнения: {time.time() - start_time:.2f} сек.')