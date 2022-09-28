from ctypes.wintypes import PINT


sa = float(input('Salário atual: R$'))
sn = sa + (sa*0.15)

print(f'O salário novo é R${sn:.2f}')