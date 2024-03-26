def dobra(lst):
    val.clear()
    for v in lst:
        v *= 2
        val.append(v)
    print(val)


val = [8, 3, 2, 7]

dobra(val[:])
