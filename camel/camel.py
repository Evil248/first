camel_name=input("camelCase:")
snake_name=""
for letter in camel_name:
    if letter.isupper():
        snake_name+= "_" + letter.lower()
    else:
        snake_name += letter
print("snake_case:", snake_name)