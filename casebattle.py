import random

bronze = ["Lamborghini", "500Coin", "Lada Granta"]
silver = ["1000Coin", "Rolls Royce", "Porsche911", "300$"]

while True:
    print("\nКакой кейс открыть?")
    print("1 — Бронзовый")
    print("2 — Серебряный")
    print("0 — Выход")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        prize = random.choice(bronze)
        print("📦 Бронзовый кейс →", prize)

    elif choice == "2":
        prize = random.choice(silver)
        print("📦 Серебряный кейс →", prize)

    elif choice == "0":
        print("Игра окончена")
        break

    else:
        print("Нет такого кейса, попробуйте снова")