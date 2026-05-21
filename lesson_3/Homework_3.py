# """
# 1. Создай класс Circle, в котором:
# есть атрибуты класса MIN_RADIUS = 1 и MAX_RADIUS = 1000,
# метод класса is_valid_radius(cls, r), который проверяет, входит ли значение в допустимый диапазон.
# Проверь результат вызова:
# print(Circle.is_valid_radius(500))   # True
# print(Circle.is_valid_radius(1500))  # False
# """
# """
# 2. Добавь в класс Circle:
# статический метод area(radius),
# который возвращает площадь круга по формуле π * r ** 2 (используй импорт math.pi),
# инициализацию в __init__, которая сохраняет радиус,
# только если он проходит валидацию через метод is_valid_radius()
# (подумай как можно проверить значения перед тем как записать их в переменные экземпляра класса)
# Пример:
# c = Circle(10)
# print(c.area(c.radius))  # Площадь круга
# """
# """
# 3. Расширь Circle, добавив обычный метод print_info, который выводит:
# Радиус: ...
# Допустимый диапазон: [MIN, MAX]
# Метод должен использовать и self, и атрибуты класса через type(self).
#
# Пример вызова:
# c.print_info()
# """
# import math
#
#
# class Circle:
#     MIN_RADIUS = 1
#     MAX_RADIUS = 1000
#
#     @classmethod
#     def is_valid_radius(cls, radius):
#         return cls.MIN_RADIUS <= radius <=cls.MAX_RADIUS
#     @staticmethod
#     def area(radius):
#         return math.pi * radius ** 2
#     def __init__(self, radius):
#         if not self.is_valid_radius(radius):
#             raise ValueError("Некорректный радиус")
#         self.radius = radius
#     def print_info(self, radius:int):
#         return self.radius
# c = Circle(5)
# print(c.area(c.radius))
# print(c.print_info(25))
# print(Circle.is_valid_radius(500))
# print(Circle.is_valid_radius(1500))

class User:
    def __init__(self):
        self.__login = None
        self.__password = None
    def __encrypt_password(self, password):
        return password.upper()
    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = self.__encrypt_password(password)
    def get_credentials(self):
        return self.__login, self.__password
    def check_password(self, password):
        return self.__encrypt_password(password) == self.__password
us = User()
us.set_credentials("jack", "amam")
print(us.get_credentials())
print(us.check_password("amam"))
print(us.check_password("qwe"))
print(us.__encrypt_password)
print(us.__password)
print(us._User__password)