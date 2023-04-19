import math
# Упражнение 1 Вывод почтового адреса
def task1():
    print("Alexey Emelyanov")
    print("9aleshaeboshu1@gmail.com")

# Упражнение 2 Приветствие
def task2():
    name = input("Введите ваше имя >>> ")
    print(name)

# Упражнение 3 Площадь комнаты
def task3():
    length = int(input("Введите длину >>> "))
    weigth = int(input("Введите ширину >>> "))
    squere = length * weigth
    print(f"Площадь комнаты: {squere:.2f}")

# Упражнение 4 Площадь садового участка
def task4():
    length = int(input("Введите длину садового участка >>> "))
    weigth = int(input("Введите ширину садового участка >>> "))
    squere = length * weigth
    print(f"В одном акре содержится {squere:.2f} квадратных футов")

# Упражнение 5 Сдаем бутылки
def task5():
    # Запрос количества бутылок каждого размера
    small_bottles = int(input("Введите количество бутылок объемом 1 литр и меньше: "))
    large_bottles = int(input("Введите количество бутылок большего объема: "))

    # Рассчет суммы
    total = small_bottles * 0.1 + large_bottles * 0.25

    # Вывод результата
    print("Сумма, которую можно выручить за сдачу бутылок: ${:.2f}".format(total))

# Упражнение 6 Налоги и чаевые
def task6():
    # Запрос суммы заказа
    order_amount = float(input("Введите сумму заказа: "))

    # Рассчет налога (пример налоговой ставки 8%)
    tax_rate = 0.08
    tax_amount = order_amount * tax_rate

    # Рассчет чаевых (18% от суммы заказа без учета налога)
    tip_rate = 0.18
    tip_amount = (order_amount - tax_amount) * tip_rate

    # Рассчет общей суммы
    total_amount = order_amount + tax_amount + tip_amount

    # Вывод результатов
    print("Налог: ${:.2f}".format(tax_amount))
    print("Чаевые: ${:.2f}".format(tip_amount))
    print("Итого: ${:.2f}".format(total_amount))

# Упражнение 7 Сумма первых n положительных чисел
def task7():
    number = int(input("Введите n >>> "))
    print((number * (number + 1)) / 2)

# Упражнение 8. Сувениры и безделушки
def task8():
    souvenir_count = int(input("Введите количество сувениров >>> "))
    souvenir_weigth = 75 * souvenir_count
    bauble_count = int(input("Введите количество безделушек >>> "))
    bauble_weigth = 112 * bauble_count
    print(f"Общий вес сувенира = {souvenir_weigth} г.")
    print(f"Общий вес безделушки = {bauble_weigth} г.")

# Упражнение 9. Сложные проценты
def task9():
    deposit = int(input("Введите сумму первого депозита >>> "))
    interest_rate = 0.04
    # Вычисляем сумму на счету через год
    balance_year_1 = round(deposit * (1 + interest_rate), 2)

    # Вычисляем сумму на счету через два года
    balance_year_2 = round(deposit * (1 + interest_rate) * (1 + interest_rate), 2)

    # Вычисляем сумму на счету через три года
    balance_year_3 = round(deposit * (1 + interest_rate) * (1 + interest_rate) * (1 + interest_rate), 2)

    # Выводим результаты
    print("Сумма на счету через 1 год:", balance_year_1)
    print("Сумма на счету через 2 года:", balance_year_2)
    print("Сумма на счету через 3 года:", balance_year_3)

# Упражнение 10. Арифметика
def task10():
    first_value = int(input("Введите 1 число >>> "))
    second_value = int(input("Введите 2 число >>> "))
    print(f"Сумма a и b = {first_value + second_value}")
    print(f"Разница a и b = {first_value - second_value}")
    print(f"Произведение a и b = {first_value * second_value}")
    print(f"Частное от деления a на b = {first_value / second_value}")
    print(f"Остаток от деления a на b = {first_value % second_value}")
    print(f"Десятичный логарифм числа a = {math.log(first_value)}")
    print(f"Результат возведения числа a в степень b = {first_value ** second_value}")

# Упражнение 11. Потребление топлива
def task11():
    mpg = float(input("Введите потребление топлива в милях на галлон: "))

    # Вычисляем потребление топлива в литрах на 100 км
    l_per_100km = round(235.215 / mpg, 2)

    # Выводим результат
    print("Потребление топлива в литрах на 100 км:", l_per_100km)

def task12():
    t1 = math.radians(float(input("Введите t1: ")))
    g1 = math.radians(float(input("Введите g1: ")))
    t2 = math.radians(float(input("Введите t2: ")))
    g2 = math.radians(float(input("Введите g2: ")))

    print(6371.01 * math.acos(math.sin(t1) * math.sin(t2) 
                              + math.cos(t1) * math.cos(t2) 
                              * math.cos(g1 - g2)))

def task13():
    ##
    # Рассчитываем минимальное количество монет для представления указанной суммы
    ##
    CENTS_PER_TOONIE = 200
    CENTS_PER_LOONIE = 100
    CENTS_PER_QUARTER = 25
    CENTS_PER_DIME =10
    CENTS_PER_NICKEL =5
    # Запрашиваем у пользователя сумму в центах
    cents = int(input("Введите сумму в центах: "))
    # Определим количество двухдолларовых монет путем деления суммы на 200. Затем вычислим
    # оставшуюся сумму для размена, рассчитав остаток от деления
    print(" ", cents // CENTS_PER_TOONIE, "двухдолларовых монет")
    cents = cents % CENTS_PER_TOONIE
    # Повторяем эти действия для остальных монет
    print(" ", cents // CENTS_PER_LOONIE, "однодолларовых монет")
    cents = cents % CENTS_PER_LOONIE
    print(" ", cents // CENTS_PER_QUARTER, "25-центовых монет")
    cents = cents % CENTS_PER_QUARTER
    print(" ", cents // CENTS_PER_DIME, "10-центовых монет")
    cents = cents % CENTS_PER_DIME
    print(" ", cents // CENTS_PER_NICKEL, "5-центовых монет")
    cents = cents % CENTS_PER_NICKEL
    # Отобразим остаток в центах
    print(" ", cents, "центов")

def task14():
    IN_PER_FT = 12
    CM_PER_IN = 2.54
    print("Введите рост: ")
    feet = int(input("Количество футов: "))
    inches = int(input("Количество дюймов: "))
    cm = (feet * IN_PER_FT + inches) * CM_PER_IN
    print(f"Ваш рост в сантиметрах: ", cm)


def main():
    #task1()
    #task2()
    #task3()
    #task4()
    #task5()
    #task6()
    #task7()
    #task8()
    #task9()
    #task10()
    #task11()
    #task12()
    #task13()
    task14()

if __name__ == "__main__":
    main()