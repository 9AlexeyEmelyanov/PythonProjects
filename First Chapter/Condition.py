# Упражнение 26. Чет или нечет?
def task26():
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print(f"Число {number} - четное")
    else:
        print(f"Число {number} - не четное")

def main():
    task26()


if __name__ == "__main__":
    main()