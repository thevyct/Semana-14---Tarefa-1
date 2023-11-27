#Dadas duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.

def cria_lista():
    lista = []
    for i in range(20):
        numeros = int(input())
        lista.append(numeros)
    return lista

def soma_valores_lista(lista_um, lista_dois):
    lista_valores_somados = []
    if (isinstance(lista_um, list) and isinstance(lista_dois, list)):
        for i in range(20):
            lista_valores_somados.append(lista_um[i]+lista_dois[i])
    return lista_valores_somados

def main():
    lista_um = cria_lista()
    lista_dois = cria_lista()
    resultado = soma_valores_lista(lista_um, lista_dois)
    print(f'{lista_um}\n{lista_dois}\n{resultado}')

if __name__ == "__main__":
    main()