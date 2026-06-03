# 1. Создай класс SecureData, который:
#
# имеет атрибут __secret, задаваемый в __init__;
# переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
# внутри класса доступ к __secret должен работать.
# Проверь:
# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"

# class SecureData:
#     def __init__(self, password):
#         self.__secret = password
#     def __getattribute__(self, item):
#         if item == "_SecureData__secret":
#             raise ValueError("Засекреченный атрибут")
#         return super().__getattribute__(item)
#     def __setattr__(self, key, value):
#         if key == "token":
#            raise AttributeError("Нельзя создавать аттрибут с таким именем")
#         return super().__setattr__(key, value)
#     def get_secret(self):
#         return object.__getattribute__(self, "_SecureData__secret")
# data = SecureData("пароль123")
# try:
#     print(data.__secret)
#     print(data.get_secret())
# except AttributeError:
#     raise "Error"
# 2. Добавь в класс SecureData метод __setattr__,
# который запрещает создание любого атрибута с именем token.
#
# Проверь:
# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает
# data.token = "abc123"
# print(data.token)
# data.other = "ok"
# print(data.other)

# 3. Создай класс SafeDict, в котором:
#
# нет атрибута default;
# реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
# реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
# Проверь:
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"
# class SafeDict:
#     def __init__(self):
#         pass
#     def __getattr__(self, name):
#         return "N/A"
#     def __delattr__(self, name):
#         print(f"Удалён атрибут {name}")
#         super().__delattr__(name)
# d = SafeDict()
# print(d.unknown)
# d.key = 10
# # del d.key
# print(d.key)

# 4. Создай класс Employee с приватными полями __name и __salary.
# Добавь @property для поля salary, а также сеттер с валидацией:
#
# зарплата должна быть положительным числом;
# если нет — выбрасывать ValueError.
# Проверь, что:
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError
# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             raise ValueError("Salary must be greater than zero")
#         self.__salary = value
#     @salary.deleter
#     def salary(self):
#         del self.__salary
#         print("Salary has been deleted")
#
# e = Employee("Daniil", 5000)
# # print(e.salary)
# # e.salary = 8000
# # print(e.salary)
# # e.salary = -100
# del e.salary
# print(e.__dict__)  # salary нет
# 6. Представь, что ты пишешь обёртку над HTML-формой.
# Создай класс LoginForm с полем username, которое реализовано через @property.
#
# Логика:
# геттер возвращает self._username
# сеттер добавляет лог "username изменён"
# Проверь, что:
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"
# class LoginForm:
#     def __init__(self):
#         self._username = None
#     @property
#     def username(self):
#         return self._username
#     @username.setter
#     def username(self, value):
#         self._username = value
#         print(f"-->LOG: username изменен: {value}")
#
# form = LoginForm()
# form.username = "admin"
# print(form.username)

import datetime

# class Card:
#     def __init__(self, number):
#         self.__number = number
#
#     @property
#     def number(self):
#         last_four = self.__number[-4:]
#         return f"**** **** **** {last_four}"
#
#     @number.setter
#     def number(self, new_number):
#         if len(new_number) != 16 or not new_number.isdigit():
#             raise ValueError("Номер карты должен состоять строго из 16 цифр!")
#         self.__number = new_number
#
#     @number.deleter
#     def number(self):
#         del self.__number
#         print(f"--> LOG: Номер карты успешно удален.")
#
# c1 = Card("1234567890123456")
# assert c1.number == "**** **** **** 3456", "Ошибка: маска работает неверно!"
# print(c1.number)
# del c1.number

class UserData:
    def __init__(self,
                 email: str,
                 age: int,
                 is_active: bool,
                ):
        self.email = email
        self.age = age
        self.is_active = is_active
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Некорректный email: отсутствует символ '@'")
        self._email = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 18 or not isinstance(value, int):
            raise ValueError("Некорректный возраст")
        self._age = value
    @property
    def json(self):
        return {
            "email": self.email,
            "age": self.age,
            "is_active": self.is_active
        }

# usr = UserData("tregubov@mail.ru", 10, True, )
# user = UserData("admin@crypto.io", 20, is_active=True)
# print(user.json)

try:
    user_bad_age = UserData("test@mail.com", 15, True)
    assert False, "Ошибка: класс пропустил возраст меньше 18!"
except ValueError:
    pass


# expected_json = {
#     "email": "admin@crypto.io",
#     "age": 25,
#     "is_active": True
# }
# assert user.json == expected_json, "Ошибка: несовпадение структур."