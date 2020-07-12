# Написать свой cache декоратор c максимальным размером кеша и его очисткой при необходимости.
# Декоратор должен перехватывать аргументы оборачиваемой функции
# Декоратор должен иметь хранилище, где будут сохраняться все перехваченные аргументы и результаты выполнения декорируемой функции
# Декоратор должен проверять наличие перехваченных аргументов в хранилище. Если декорируемая функция уже вызывалась с такими аргументами, она не будет вызываться снова,
# вместо этого декоратор вернет сохраненное значение.
# Декоратор должен принимать один аргумент - максимальный размер хранилища.
# Если хранилище заполнено, нужно удалить 1 любой элемент, чтобы освободить место под новый.
def do_cache(maxsize):
    cache = {}
    def decorator_cache(func):
        def wrapper(*args):
            if len(cache) >= maxsize:
                cache.popitem()
            if args in cache:
                return cache[args]
            else:
                result = func(*args)
                cache[args] = result
                return result
        return wrapper
    return decorator_cache


@do_cache(maxsize=3)
def get_value(a, b):
  return a ** b