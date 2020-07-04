def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    result_list = []
    for i in url_list:
        if '/catalog/' in i:
            result_list.append(i)

    return result_list



def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """

    if len(input_str) % 2:
        output_str = input_str[len(input_str)//2 - 1:len(input_str)//2 + 2]
    else:
        output_str = input_str[len(input_str)//2 - 1:len(input_str)//2 + 1]

    return output_str



def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """

    output_dict = {}
    for i in input_str:
        if i not in output_dict:
            output_dict.update({i:1})
        else:
            count = output_dict.get(i) + 1
            output_dict.update({i: count})

    return output_dict



def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    mid_str1 = len(str1)//2
    result_str = str1[:mid_str1] + str2 + str1[mid_str1:]

    return result_str



def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    even_int_list = list()
    from random import randint
    lst = [randint(0, 100) for _ in range(100)]

    for i in lst:
        if not i % 2 and i:             # так как 0 не является четным мы его тоже исключаем из нового списка
            even_int_list.append(i)

    return even_int_list
