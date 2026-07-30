# 1. Создай две функции: inner() и outer().
# В inner() вызови деление на ноль.
# В outer() просто вызови inner().
# Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.
# 2. Добавь вокруг вызова outer() конструкцию try/except,
# чтобы перехватить исключение и вывести сообщение
# "Ошибка перехвачена на верхнем уровне".
# 3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
# В случае ошибки возвращай строку "Ошибка в inner".
# 4. Сделай так:
# В inner() ошибка не перехватывается.
# В outer() ошибка перехватывается через try/except.
# В outer() при перехвате напечатай "Ошибка в outer".
def inner():
    return 1/0

def outer():
    try:
        inner()
    except Exception:
        print("Ошибка в outer")


inner()
outer()
from multiprocessing.managers import rebuild_as_list

def get_value():
    raise ValueError
def test_get_value():
    try:
        get_value()
    except ValueError:
        assert False, "Исключение поймано"
test_get_value()

# 5. Напиши функцию get_value(), которая кидает ValueError.
# Напиши тестовую функцию test_get_value(), которая:
#
# Вызывает get_value();
# Ловит ValueError;
# Завершает тест с assert False, если исключение поймано.
# 6. Создай функцию divide(x, y).
# Если y == 0, выбрасывай ZeroDivisionError через raise.
# Иначе возвращай результат деления.
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    else:
        return x / y
div = divide(1, 2)
print(div)
# 7. Создай функцию sqrt(x), которая:
# Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
# Иначе возвращает квадратный корень из x.
# Проверь поведение функции через try/except.
class NegativeNumberError(Exception):
    pass
def sqrt(x):
    if x <= 0:
        raise NegativeNumberError("Число не может быть отрицательным")
    return x ** 0.5
try:
    result = sqrt(7)
    print(f"Корень: {result}")
except NegativeNumberError as e:
    print(f"Ошибка: {e}")
try:
    result = sqrt(-9)
    print(f"Корень: {result}")
except NegativeNumberError as e:
    print(f"Ошибка: {e}")
# 8. Создай базовый класс MathError.
# От него унаследуй:
# NegativeNumberError
# DivisionByZeroError
# В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
# Проверь в try/except обработку ошибок через базовый класс MathError.
class MathError(Exception):
    pass

class NegativeNumberError(MathError):
    pass

class DivisionByZeroError(MathError):
    pass

def safe_divide(x, y):
    if y == 0:
        raise DivisionByZeroError("Division by zero")
    return x / y
# 9. Создай тестовую функцию test_sqrt(), которая:
# вызывает sqrt(x) с отрицательным числом;
# перехватывает NegativeNumberError;
# завершает тест с assert False и сообщением
# "Нельзя брать корень из отрицательного числа".
def test_sqrt(x):
    try:
        sqrt(-3)
    except NegativeNumberError:
        assert False, "Нельзя брать корень из отрицательного числа"


try:
    result = safe_divide(2, 0)
    print(result)
except MathError as e:
    print(f"Error: {e}")

# 10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
# Обеспечь закрытие файла через with.
import requests

def __enter__(self):
    self.session = requests.Session()

with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
# 11. Создай класс BackupList, который:
# делает копию списка при входе в with,
# при выходе сохраняет изменения, если ошибок не было,
# откатывает изменения при ошибке.
# Проверь:
# успешное изменение списка;
# откат при ошибке.
class BackupList:
    def __init__(self, original_list):
        self.original_list = original_list
        self.backup = None

    def __enter__(self):

        self.backup = self.original_list.copy()
        return self.original_list  # возвращаем сам список для работы внутри with

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:

            self.original_list[:] = self.backup
            print(f"Ошибка: {exc_val}. Изменения откачены.")
        else:

            print("Изменения успешно сохранены.")
        return True


data = [1, 2, 3]
with BackupList(data) as lst:
    lst.append(4)
    lst.append(5)

print("Результат:", data)

# 12. Создай декоратор-класс Timer,
# который измеряет время выполнения функции и выводит результат.
import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Функция '{self.func.__name__}' выполнена за {end - start:.6f} сек.")
        return result


@Timer
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
slow_function(10_000_000)