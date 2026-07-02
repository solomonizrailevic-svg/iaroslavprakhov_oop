# 1. Создай три класса: Cat, Dog, Duck.
# В каждом реализуй метод speak(), возвращающий уникальную строку.
# Создай список из экземпляров этих классов и вызови метод speak()
# в цикле.
class Cat:
    def speak(self, text):
        print(f"Cat: {text}")

class Dog:
    def speak(self, text):
        print(f"Dog: {text}")
class Duck:
    def speak(self, text):
        print(f"Duck: {text}")

zoo = [Cat(), Dog(), Duck()]

for animal in zoo:
    animal.speak("Hello")
# 2. Создай базовый класс Shape
# Создай три класса-наследника: Square, Rectangle, Triangle,
# в каждом реализуй метод get_pr().
# Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
# можно обойти в цикле и вызвать get_pr() у каждого.
# 3. Сделай класс Shape абстрактным.
# Переопредели get_pr() как @abstractmethod.
# Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_pr(self):
        pass
class Square(Shape):
    def get_pr(self):
        print("SQUARE")

class Rectangle(Shape):
    def get_pr(self):
        print("RECTANGLE")

class Triangle(Shape):
    def get_pr(self):
        print("TRIANGLE")


shapes = [Square(), Rectangle(), Triangle()]
for shape in shapes:
    shape.get_pr()

shp = Shape()

# 4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
# Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
# Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.
class A:
    def __init__(self, letter):
        print(f"init A:{letter}")
        super().__init__(letter)
class B:
    def __init__(self, letter):
        print(f"init B:{letter}")
        super().__init__(letter)
class C:
    def __init__(self, letter):
        print(f"init C:{letter}")

class D(A, B, C):
    def __init__(self, letter):
        print(f"init D:{letter}")
        super().__init__(letter)

d = D("X")

print(D.__mro__)

# 5. Создай MixinLog (как в уроке).
# Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
# Создай класс, который наследует оба класса. Создай экземпляр этого класса.
# 6. В Goods и MixinLog реализуй print_info().
# Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
# Измени порядок наследования — изменилась ли логика?
class MixinLog:
    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

class Hotel:
    def __init__(self, hotel_number, hotel_name, hotel_address):
        self.hotel_number = hotel_number
        self.hotel_name = hotel_name
        self.hotel_address = hotel_address

    def print_info(self):
        print(f"{self.hotel_number}, {self.hotel_name}, {self.hotel_address}")

class Double(Hotel, MixinLog):
    pass

client = Double(2, "Mariott", "Red Square")
client.print_info()

# 7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
# Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
# и выведи сообщение: "На ноль делить нельзя!"
# 8. Расширь программу из Задания 1:
# Добавь обработку ошибки (как называется ошибка найди сам),
# если пользователь ввёл не числа, а текст.
# Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
# 9. Модифицируй код так, чтобы после обработки конкретных ошибок
# был ещё один общий except, который перехватывает все остальные ошибки и выводит:
# "Произошла неизвестная ошибка"
# 10. При перехвате исключений из 7 и 8 заданий,
# сохрани ошибку в переменную e и выведи её текст:
class PressNumb:
    def divide(self, number_1, number_2):
            try:
                return number_1/number_2
            except ZeroDivisionError as a:
                print(f"На ноль делить нельзя! {a}")
            return None
try:
    number_1 = int(input("Введите первое число: "))
    number_2 = int(input("Введите второе число: "))
except ValueError as f:
    print(f"Ошибка ввода: введите два числа через пробел: {f}")
except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")
else:
    divider = PressNumb()
    result = divider.divide(number_1, number_2)
    print(f"результат: {result}")

# 11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
# Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
# 12. Запроси у пользователя два числа и выполни деление.
# Если деление прошло успешно без ошибок — выведи
# "Деление выполнено успешно" через (но не в блоке try)
# 13. Расширь код из Задания 12:
# Добавь блок, в котором будет выводиться
# "Работа программы завершена", независимо от успеха деления.
# 14. Реализуй две вложенные конструкции:
# Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
# Внутренний try/except ловит деление на ноль.
# 15. Вынеси обработку деления в отдельную функцию divide(x, y)
# с собственным try/except.
# Во внешнем коде обработай только ошибку ввода.
class Arfm:
    def num_mult(self):
        try:
            return num_1 / num_2
        except ArithmeticError as o:
            print(f"Арифметическая ошибка: {o}")

try:
    num_1 = int(input("Введите число: "))
    num_2 = int(input("Введите еще одно число: "))
except ValueError as e:
    print(f"Пожалуйста, введите число: {e}")
else:
    arif = Arfm()
    result = arif.num_mult()
    if result is not None:
        print(f"Деление выполнено успешно: {result}")
    print("Работа программы завершена")