def contar_caracteres(string):
    # Inicializa um dicionário vazio
    contador = {}

    # Itera sobre cada caractere da string
    for caracter in string:
        # Se o caractere já estiver no dicionário, incrementa 1
        if caracter in contador:
            contador[caracter] += 1
        else:
            # Se não estiver, adiciona ao dicionário com valor inicial 1
            contador[caracter] = 1
    
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)