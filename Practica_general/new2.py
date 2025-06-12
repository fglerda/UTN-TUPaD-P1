def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num + 1)


num = 5
suma_recursiva(num)
