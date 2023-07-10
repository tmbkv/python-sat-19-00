"""
Коротко о типах дданных
int
str
"""

# type() - проверить тип данных

# Целые числа - int - int()
print(int("12"), type(int("12")))  # Преобразование строки в число
print("12", type("12"))
print(12, type(12))
print(int(3.14))

# print(int("12e")) - ValueError

print(-432)
print(0)
print(543)
print(1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567)

# Строки - str - str()
print(str(12), type(str(12)))
print("Hello 'World'")
print('Hello "John"')
print("Hello \"World\"")
print()
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print()
print("""Commands:
1. pull
2. coomit
3. push
""")
print('''Hello''')
