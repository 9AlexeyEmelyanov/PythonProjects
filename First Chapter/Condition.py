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

def main():
    #task26()
    task27()


if __name__ == "__main__":
    main()