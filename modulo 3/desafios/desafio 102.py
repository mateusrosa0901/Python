def fatorial(num, show=False):
    """
    :param num: O número que vai ser calculado o fatorial
    :param show: False defalt, mostrar ou não a conta
    :return: O valor da fatorial do número num
    """
    fat = num
    lst = list()

    while num > 1:
        lst.append(num)
        num -= 1
        fat *= num

    print('-'*((len(lst)+3)*5))

    if show:
        for v in lst:
            print(f'{v} x ', end='')
        print('1 =', end=' ')
        return fat

    else:
        return fat

print(fatorial(5, True))
