menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0  # Инициализируем total перед циклом, чтобы сохранить сумму блюд.

while True:
    try:
        your_food = input("Item: ").title()
    except EOFError:
        print()
        break
    if your_food in menu:
        total += menu[your_food]
        print("Total: $",f"{total:.2f}", sep="")



