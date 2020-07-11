def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    temp_list = list(set(input_list))
    biggest_ints = []
    for _ in range(3):
        max_i = max(temp_list)
        biggest_ints.append(max_i)
        temp_list.remove(max_i)

    return biggest_ints


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    lowest_int_index = input_list.index(min(input_list))

    return lowest_int_index


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    reversed = input_list
    reversed.reverse()

    return reversed


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    common_keys = []
    for i in dict1:
        if i in dict2:
            common_keys.append(i)

    return common_keys


def sort_by_age(student_list):
    """
    Дан массив из словарей:
[{'name': 'Viktor', 'age': 30, 'city': 'Kiev'},
{'name': 'Andrey', 'age': 34, 'city': 'Kiev'},
{'name': 'Maksim', 'age': 20, 'city': 'Dnepr'},
{'name': 'Artem', 'age': 50, 'city': 'Dnepr'},
{'name': 'Vladimir', 'age': 32, 'city': 'Lviv'},
{'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}]

    C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {
           'Kiev': [ {'name': 'Viktor', 'age': 30 },
                        {'name': 'Andrey', 'age': 34}],
           'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                           {'name': 'Artem', 'age': 50}],
           'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                        {'name': 'Dmitriy', 'age': 21}]
        }
    """
    student_list.sort(key=lambda k: k['age'])
    sorted_dict = {}
    for i in student_list:
        town = i['city']
        if town not in sorted_dict:
            sorted_dict[town] = [{'name':i['name'],'age':i['age']}]
        else:
            sorted_dict[town].append({'name':i['name'],'age':i['age']})

    return sorted_dict

