"""Realizar la suma de los primeros n valores positivos de forma recursiva"""


def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num - 1)


if __name__ == "__main__":
    print(suma_recursiva(10))
