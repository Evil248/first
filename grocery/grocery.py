itemss = {}


while True:
    try:
        your_item = input().upper()


    except EOFError:
        print()
        break


    if your_item in itemss:
        itemss[your_item] += 1
    else:
        itemss[your_item] = 1


for your_item in sorted(itemss.keys()):
        print(itemss[your_item], your_item)