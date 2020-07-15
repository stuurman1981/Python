# 1. Напишите функцию, которая возвращает список файлов из директории.
# 2. Напишите декоратор для этой функции, который распечатает все файлы с
# раcширением .log из найденных
import os
def log_reader(func):
    def wrapper(*args):
        folder = func(*args)
        for file in folder:
            if file.endswith(".log"):
                full_path = f"{str(args[0])}{os.sep}{file}"
                with open(f"{full_path}", 'r') as log_file:
                    print(f'Content of {file} is:')
                    print(log_file.read())
        return folder
    return wrapper

@log_reader
def file_list(path):
    return os.listdir(path)
