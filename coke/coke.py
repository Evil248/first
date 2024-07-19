amount_coins = 0

while amount_coins < 50:
    coins = int(input("Insert Coin: "))

    if coins == 5:
        amount_coins += 5
    elif coins == 10:
        amount_coins += 10
    elif coins == 25:
        amount_coins += 25

    # Проверяем, не превышает ли сумма внесенных монет 50 центов
    if amount_coins < 50:
        print("Amount Due:", 50 - amount_coins)
    else:
        print("Change Owed:", amount_coins - 50)
