# """
# Задание 1
# 1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
# Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
# Проверь, как это повлияло на значения у обоих объектов.
# Убедись, что __dict__ объектов отражает изменения.
# """
class Dog:
    "Друг человека"
    species = "canis"
    legs = 4
    name = "Бобик"
    age = 2
bulldog = Dog()
chihuahua = Dog()
bulldog.species = "vulpes"
chihuahua.legs = 5
print(bulldog.species)
print(chihuahua.legs)
print(bulldog.__dict__)
print(chihuahua.__dict__)
# """
# Задание 2
# 2. Добавь в класс Dog строку документации, описывающую его назначение.
# Затем выведи её на экран.
# После этого добавь в объект класса новые атрибуты name и age,
# а затем удали name.
# Проверь, что произойдёт при попытке снова вывести объект.name.
# """
print(Dog.__doc__)
del Dog.name
print(Dog.name)
# """
# Задание 3
# 3. Создай класс User с атрибутами класса role = "guest" и active = True.
# С помощью функций getattr(), setattr(), hasattr() и delattr():
#
# измени значение role на "admin",
# проверь наличие active,
# добавь новый атрибут email,
# удали role.
# Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.
# """
class User:
    role = "guest"
    active = True
setattr(User, 'role', 'admin')
setattr(User, "email", "ttt@mail.ru")
print(User.role)
print(getattr(User, 'active'))
print(User.email)
delattr(User, "role")
print(User.__dict__)    