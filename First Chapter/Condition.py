import math
# Упражнение 26. Чет или нечет?
def task26():
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print(f"Число {number} - четное")
    else:
        print(f"Число {number} - не четное")

# Упражнение 27. Собачий возраст
def task27():
    human_age = int(input("Введите возраст в годах: "))
    if human_age < 0:
        print("Ошибка: возраст не может быть отрицательным.")
    else:
        if human_age <= 2:
            dog_age = human_age * 10.5
        else:
            dog_age = 10.5 * 2 + (human_age -2) * 4
        print("Собачий возраст: {:.1f} лет".format(dog_age))

# Упражнение 28. Гласные и согласные
def task28():
    letter = input("Введите латинскую букву: ")
    letter.lower()
    if letter == 'a' or letter == 'e' \
        or letter == 'i' or letter == 'o' or letter == 'u':
        print("Это гласная буква")
    elif letter == 'y':
        print("Это гласная и согласная буква")
    elif letter.isdigit():
        print("Это число")
    else:
        print("Это согласная буква")

# Упражнение 29. Сколько дней в месяце?
def task29():
    month = input("Введите название месяца: ")
    days = 31
    if month == "Апрель" or month == "Июнь" or \
        month == "Сентябрь" or month == "Ноябрь":
        days = 30
    elif month == "Февраль":
        days = "28 или 29"
    print("Количество дней в месяце", month, "равно", days) 

def main():
    #task26()
    #task27()
    #task28()
    task29()

if __name__ == "__main__":
    main()