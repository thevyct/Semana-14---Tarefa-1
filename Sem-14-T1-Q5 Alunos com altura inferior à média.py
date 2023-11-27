#Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos.

def cria_lista():
    lista_nome_alunos = []
    lista_idade_alunos = []
    lista_alturas_alunos = []
    for i in range(30):
        nome = input()
        lista_nome_alunos.append(nome)
        idade = int(input())
        lista_idade_alunos.append(idade)
        altura = float(input())
        lista_alturas_alunos.append(round(altura, 2))
    return lista_nome_alunos, lista_idade_alunos, lista_alturas_alunos

def media_altura_alunos(lista_alturas):
    soma = 0
    for i in lista_alturas:
        soma += i
    media = soma/30
    return round(media, 2)

def alunos_altura_inferior_media(lista_idades, media, lista_altura, lista_nomes):
    for i in range(30):
        if lista_idades[i] > 13:
            if lista_altura[i] < media:
                print(f'{lista_nomes[i]}')

def main():
    lista_de_nomes_de_alunos, lista_de_idades_de_alunos, lista_de_alturas_de_alunos = cria_lista()
    media = media_altura_alunos(lista_de_alturas_de_alunos)
    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    alunos_altura_inferior_media(
        lista_de_idades_de_alunos, media, lista_de_alturas_de_alunos, lista_de_nomes_de_alunos)

if __name__ == "__main__":
    main()