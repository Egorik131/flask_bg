'''Задание №9
� Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
� Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
� Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
� Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
� Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.'''

import time
import requests
import asyncio
import aiohttp

urls = [
        'https://rare-gallery.com/uploads/posts/795837-Cats-Eyes-Glance-Whiskers-Snout-Nose.jpg',
        'https://wallbox.ru/wallpapers/main/201546/13dcd7162ea7a31.jpg',
        'https://i.pinimg.com/originals/5b/e2/56/5be25606a1b0a0e951600ec09c4147f1.jpg',
        'https://i.artfile.ru/2137x1412_600336_[www.ArtFile.ru].jpg',
        ]

start_time = time.time()

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            filename = url[-10:]
            with open(filename, 'bw') as f:
                f.write(await response.read())
                print(f'Файл {url} скачан за {time.time() - start_time:.2f}')

async def main():
    tasks =[]
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())