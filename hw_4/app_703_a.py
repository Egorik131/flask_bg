'''Задание №7
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.'''

'''Асинхронность'''

import time
import asyncio
from random import randint

my_arr = [randint(1, 100) for i in range(1_000_000)]
summ_elem = 0


async def summa_elements(arr):
    global summ_elem
    for i in range(len(arr)):
        summ_elem += arr[i]
    print(f'Сумма элементов массива: {summ_elem:_}. Время выполнения: {time.time() - start_time:.2f} сек.')


async def main():
    tasks = []
    parts = 5
    piece_arr = len(my_arr) // parts
    for i in range(parts):
        task = asyncio.create_task(summa_elements(my_arr[piece_arr * i:piece_arr * (i + 1)]))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Общее время выполнения: {time.time() - start_time:.2f} сек.')
