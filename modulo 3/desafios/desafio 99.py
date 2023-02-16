def maior(* num):
    print('='*15)
    m = 0
    for n in num:
        print(n, end=' -> ')
        if n >= m:
            m = n
    print('FIM')
    print(f'O maior número é: {m}')
    print('='*15)


maior(5, 8, 4, 7, 45, 8, 7, 6, 3, 5, 1)
maior(2, 3, 5, 12, 47, 85, 41, 78, 93, 62)
