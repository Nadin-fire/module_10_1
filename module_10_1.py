from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    """Ведет запись слов в соответствующий файл
    с прерыванием после записи каждого на 0.1 секунду:
    word_count - количество записываемых слов,
    file_name - файл для записи (название)"""
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
                file.write(f'Какое-то слово № {i + 1}\n')
                sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

start_time = datetime.now() # Взятие текущего времени

# Запуск функций
write_words(10, 'example1.txt')
write_words (30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

datetime.now() # Взятие текущего времени

print(f'Работа потоков: {datetime.now() - start_time}') # Вывод разницы начала и конца работы функций

start_time_thread = datetime.now() # Взятие текущего времени

# Создание потоков
thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = Thread(target=write_words, args=(100, 'example8.txt'))

# Запуск потоков
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()
thread3.join()
thread4.join()

datetime.now() # Взятие текущего времени

print(f'Работа потоков: {datetime.now() - start_time_thread}') # Вывод разницы начала и конца работы потоков
