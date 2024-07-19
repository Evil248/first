n=input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip()
norm_n= n.lower()
if norm_n == '42' or norm_n == 'forty-two' or norm_n== 'forty two':
    print('YES')
else:
    print('NO')