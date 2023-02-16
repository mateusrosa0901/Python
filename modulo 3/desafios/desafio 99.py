def maior(* num):
    m = 0
    for n in num:
        print(n, end=' -> ')
        if n >= m:
            m = n
    print(f'O maior número é: {m}')


maior(5, 8, 4, 7, 45, 8, 7, 6, 3, 5, 1)