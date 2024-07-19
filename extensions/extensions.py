file_name = input("Введите имя файла: ").strip()
file_extension = file_name.split('.')[-1].lower()
file_first=file_name.split('.')[0].lower()

if file_extension == 'jpeg' or file_extension == 'jpg':
    print('image/jpeg')
elif file_extension in [ 'png',  'gif']:
    print('image/' + file_extension)
elif file_extension == 'pdf'or file_extension == 'zip':
    print('application/' + file_extension)
elif file_extension == 'text' or file_extension == 'txt':
    print('text/' + file_first)
else:
    print('application/octet-stream')
