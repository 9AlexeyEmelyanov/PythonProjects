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

# Упражнение 12. Расстояние между точками на Земле
def task12():
    t1 = math.radians(float(input("Введите t1: ")))
    g1 = math.radians(float(input("Введите g1: ")))
    t2 = math.radians(float(input("Введите t2: ")))
    g2 = math.radians(float(input("Введите g2: ")))

    print(6371.01 * math.acos(math.sin(t1) * math.sin(t2) 
                              + math.cos(t1) * math.cos(t2) 
                              * math.cos(g1 - g2)))

# Упражнение 13. Размен
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


# Упражнение 14. Рост
def task14():
    IN_PER_FT = 12
    CM_PER_IN = 2.54
    print("Введите рост: ")
    feet = int(input("Количество футов: "))
    inches = int(input("Количество дюймов: "))
    cm = (feet * IN_PER_FT + inches) * CM_PER_IN
    print(f"Ваш рост в сантиметрах: ", cm)

# Упражнение 15. Расстояние
def task15():
    # 1 feet = 12 inches 
    FT_PER_IN = 12
    # 1 feet = 0.33 yards 
    FT_PER_YR = 0.33
    # 1 feet = 0.00019 miles 
    FT_PER_ML = 0.00019

    print("Введите расстояние в футах:")
    feet = float(input())
    inches = feet * FT_PER_IN
    yards = feet * FT_PER_YR
    miles = feet * FT_PER_ML
    print(f"{feet:.2f} футы - это {inches:.2f} дюймов,"
           f"{yards:.2f} ярдов и {miles:.5f} миль")

# Упражнение 16. Площадь и объем
def task16():
    r = float(input("Введите радиус фигуры: "))
    area = math.pi * math.pow(r, 2.0)
    volume = (4 * math.pi * math.pow(r, 3.0)) / 3
    print(f"Площадь фигуры: {area}, объем фигуры: {volume}")

# Упражнение 17. Теплоемкость
def task17():
    # q = mCdT.
    WATER_HEAT_CAPACITY = 4.186
    ELECTRICITY_PRICE = 8.9
    J_TO_KWH = 2.777e-7

    volume = float(input("Объем воды в миллилитрах: "))
    d_temp = float(input("Повышение температуры (в градусах Цельсия): "))
    q = volume * d_temp * WATER_HEAT_CAPACITY
    print(f"Потребуется {q} Дж энергии.")
    kwh = q * J_TO_KWH
    cost = kwh * ELECTRICITY_PRICE
    print(f"Стоимость энергии: {cost:.2f} центов.")

# Упражнение 18. Объем цилиндра
def task18():
    r_cilinder = int(input("Введите радиус цилиндра: "))
    h_cilinder = int(input("Введите высоту цилиндра: "))
    volume = round(math.pi * math.pow(r_cilinder, 2.0) * h_cilinder, 1)
    print(f"Объем цилиндра: {volume:.1f}")

# Упражнение 19. Свободное падение
def task19():
    GRAVITY = 9.8
    heigth = int(input("Введите высоту в метрах: "))
    vf = math.sqrt(2 * GRAVITY * heigth)
    print(f"Объект дистигнет земли на скорости: {vf:.2f}")


# Упражнение 20. Уравнение состояния идеального газа
def task20():
    # Формула - PV = nRT
    R_COST = 8.314
    pressure = float(input("Введите давление в Па: "))
    volume = float(input("Введите объем газа в литрах: "))
    temperature = float(input("Введите температуру в градусах Цельсиях: "))

    # Преобразовать температуру в Кильвины
    temperature_K = temperature + 273.15

    # Рассчитать количество вещества в молях
    n = (pressure * volume) / (R_COST * temperature_K)

    # Вывести результат
    print(f"Количество газа в молях: {n:.2f}")

# Упражнение 21. Площадь треугольника
def task21():
    b = int(input("Введите длину треугольника: "))
    h = int(input("Введите высоту треугольника: "))
    area = b * h / 2
    print(f"Площадь треугольника = {area:.2f}")

# Упражнение 22. Площадь треугольника (снова)
def task22():
    s1 = int(input("Введите 1 длину треугольника: "))
    s2 = int(input("Введите 2 длину треугольника: "))
    s3 = int(input("Введите 3 длину треугольника: "))
    s = (s1 + s2 + s3) / 2
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
    print(f"Площадь треугольника = {area:.2f}")

# Упражнение 23. Площадь правильного многоугольника
def task23():
    s = int(input("Введите длину стороны: "))
    n = int(input("Введите количество сторон: "))
    area = n * math.pow(s, 2.0) / 4 * math.tan(math.pi / n)
    print(f"Площадь треугольника = {area:.2f}")

# Упражнение 24. Единицы времени
def task24():
    MIN_PER_SEC = 60
    HOURS_PER_SEC = MIN_PER_SEC * 60
    DAYS_PER_SEC = HOURS_PER_SEC * 24  
    
    days = int(input("Введите кол-во дней: "))
    hours = int(input("Введите кол-во часов: "))
    minutes = int(input("Введите кол-во минут: "))
    seconds = int(input("Введите кол-во секунд: "))
    print(f" {days} дней в секунды: {DAYS_PER_SEC * days}")
    print(f" {hours} часов в секунды: {HOURS_PER_SEC * hours}")
    print(f" {minutes} минут в секунды: {MIN_PER_SEC * minutes}")

# Упражнение 25. Сумма цифр в числе
def task25():
    number = 314
    first_number = number // 100
    second_number = (number // 10) % 10
    third_number = number % 10
    sum = first_number + second_number + third_number
    print(sum)

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
    #task14()
    #task15()
    #task16()
    #task17()
    #task18()
    #task19()
    #task20()
    #task21()
    #task22()
    #task23()
    #task24()
    task25()

if __name__ == "__main__":
    main()