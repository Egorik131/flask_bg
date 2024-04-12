'''Задание №7
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.'''

'''Многопоточность'''

from random import randint
import threading
import time

my_arr = [randint(1, 100) for i in range(1_000_000)]
start_time = time.time()
summ_elem = 0


def summ_elements(arr):
    global summ_elem
    for i in range(len(arr)):
        summ_elem += arr[i]
    print(f'Сумма элементов массива: {summ_elem:_}. Время выполнения: {time.time() - start_time:.2f} сек.')


threads = []
parts = 10
piece_arr = len(my_arr) // parts
for i in range(parts):
    t = threading.Thread(target=summ_elements, args=(my_arr[piece_arr * i:piece_arr * (i + 1)],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Общее время выполнения: {time.time() - start_time:.2f} сек.')
