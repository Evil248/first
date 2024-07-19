import inflect
p = inflect.engine()
lst = []
while True :
    try:
        name=input("Names:")
        lst.append(name)
    except EOFError:
        print("/n")
        break
for name in lst:
    my_l=p.join((lst), final_sep=",")
print(f"Adieu, adieu, to {my_l}")