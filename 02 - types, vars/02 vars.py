number = 10  # переменная - ссылка на ячейку памяти

# print(5)
number10 = number
print(number)
print(number10)

print(id(number))  # узнать адрес ячейки памяти
print(id(number10))  # узнать адрес ячейки памяти
print()
# int, str - неизменяемый тип данных

number = 11
print(number)
print(id(number))
print(number10)
print(id(number10))

print()

text = "Привет"
print(text)
print(id(text))

text = text + " " + "Мир"
print(text)
print(id(text))

print()
# Резервирование памяти
number20 = 20
print(id(number20))
print(id(2 * 10))
print(id(10 + 10))

print()
world = "Hello"
print(id(world))
print(id("Hell" + "o"))
