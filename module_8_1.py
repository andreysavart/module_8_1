def add_everything_up(a, b):
    try:
        # Пробуем сложить a и b
        return a + b
    except TypeError:
        # Если возникает TypeError, возвращаем строковое представление a и b вместе
        return f"{a}{b}"

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))         # 130.456