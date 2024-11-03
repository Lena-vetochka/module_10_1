"""
Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов,
file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с
прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков.
"""
import threading
from time import sleep
import datetime

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.datetime.now()
time_res = time_stop - time_start
print(f'Работа потоков {time_res}')

time_start2 = datetime.datetime.now()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args= (30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args= (200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args= (100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time_stop2 = datetime.datetime.now()
time_res2 = time_stop2 - time_start2
print(f'Работа потоков {time_res2}')

