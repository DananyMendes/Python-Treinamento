def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([1999999, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(1999999))  # (9, 11)