def calcular_total(valor, taxa):
    if valor < 0:
        return 0

    total = valor + (valor * taxa)
    print("Total calculado:", total)

    return total