a = [1 , 2 , 3]
b = a #linka
b = a[:] #copia

b.append(4)
print(a)
print(b)