#Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura dos jogadores, determine: a. o nome e a altura do jogador mais alto; b. a média de altura do time; c. os jogadores com altura superior à média, listando o nome e a altura de cada um.

def cria_lista():
    lista_nome_jogadores = []
    lista_numero_jogadores = []
    for i in range(12):
        nome = input()
        lista_nome_jogadores.append(nome)
        numero = float(input())
        lista_numero_jogadores.append(numero)
    return lista_nome_jogadores, lista_numero_jogadores

def altura_jogador_mais_alto(lista_nome, lista_numero):
    altura_maxima = max(lista_numero)
    contador = 0
    for i in lista_numero:
        if i == altura_maxima:
            break
        contador += 1
    return lista_nome[contador], altura_maxima

def media_altura(lista_alturas):
    soma = 0
    for i in lista_alturas:
        soma += i
    media = soma/12
    return media

def maior_que_media_altura(lista_alturas, lista_nome, media):
    
    if (isinstance(lista_alturas, list) and isinstance(lista_nome, list)):
        for i in range(12):
            if lista_alturas[i] > media:
                print(f'{lista_nome[i]}')
                print(f'{lista_alturas[i]:.2f}')
    
def main():
    lista_jogadorers, lista_altura_jogadores = cria_lista()
    nome_jogador_mais_alto, altura_do_jogador_mais_alto = altura_jogador_mais_alto(lista_jogadorers, lista_altura_jogadores)
    media_altura_time = media_altura(lista_altura_jogadores)
    print(f'JOGADOR MAIS ALTO DO TIME\n{nome_jogador_mais_alto}\n{altura_do_jogador_mais_alto:.2f}')
    print(f'ALTURA MÉDIA DO TIME\n{media_altura_time:.2f}')
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    maior_que_media_altura(lista_altura_jogadores, lista_jogadorers, media_altura_time)

if __name__ == "__main__":
    main()