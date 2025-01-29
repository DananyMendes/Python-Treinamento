def verificador_ano_bissexto():
    ano = int(input())

    # Verifica se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")  # Saída para ano bissexto
    else:
        print("NÃO")  # Saída para ano não bissexto
verificador_ano_bissexto()