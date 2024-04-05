def leiaDinheiro():
    while True:
        valor = input('Digite um valor: R$')

        if ',' in valor:
            valor = valor.replace(',', '.')

        try:
            valor = float(valor)
            return valor

        except ValueError:
            print('\033[1;91mErro: Tipo digitado inválido.\033[m')
