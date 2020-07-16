# 1. Напишите функцию, которая читает и распечатывает текстовый файл.
# 2. Напишите декоратор к этой функции, который печатает название файла и количество слов в нем
import os
def words_count(func):
    def wrapper(*args):
        file_name = args[0].split('/')[-1]
        result = func(*args)
        text = result.split(' ')
        count = 0
        for _ in text:
            count += 1
        print(f'File: {file_name} has {count} words.\n')
        return result
    return wrapper


@words_count
def file_reader(file):
    with open(file, 'r') as open_file:
        return open_file.read()
