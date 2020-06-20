from sys import exit
from random import choice
from emoji import emojize
from time import sleep
# import funforca (Módulo criado para as funções do jogo!)


# MAXIMIZE AO MÁXIMO A TELA QUANDO FOR EXECUTAR
# O CÓDIGO PARA O ENQUADRAMENTO CORRETO DO JOGO!


def tempo():
    """Esta função cria um intervalo de tempo de 1,5 segundos
     para a próxima linha de comando do código!"""
    sleep(1.5)


def tempo_final():
    """Esta função cria um intervalo de tempo de 5 segundos
    para a próxima linha de comando do código!"""
    sleep(5)


def limpa_tela():
    """Esta função limpa a tela do programa!"""
    print('\n' * 30)


def muda_letra():
    """Esta função muda o espaço tracejado da palavra sorteada por uma letra
     escolhida pelo usuário, quando essa mesma letra é existente na palavra sorteada!"""
    global letra, palavra, letras_encontradas
    return_tmp = ''
    for p, l in enumerate(palavra):
        if l == letra:
            return_tmp += l
        else:
            return_tmp += letras_encontradas[p]
    return return_tmp


def mostra_letras_encontradas():
    """Esta função mostra na tela do jogo durante a partida as letras existentes
    na palavra sorteada de acordo com que elas são descobertas pelo usuário!"""
    global letras_encontradas
    print((center - len(letras_encontradas) + 3) * ' ', end='')
    for l in letras_encontradas:
        print(l + ' ', end='')
    print('\n')


def mostra_letras_usadas():
    """Esta função é responsável por mostrar na tela do jogo durante a partida todas
     as letras utilizadas pelo usuário na tentativa de descobrir qual é a palavra!"""
    global letras_usadas
    print((center - 4) * ' ' + 'LETRAS USADAS:')
    print((center - int(len(letras_usadas) / 2) + 5) * ' ', end='')
    for l in letras_usadas[0:-2]:
        print(l, end='')
    print('\n')


def forca():
    """Esta função é responsável pelo desenho da forca e pelo desenho das partes do
    corpo a cada erro cometido pelo usuário na tentativa da descoberta da palavra!"""
    global partes_do_corpo, center, erro
    if erro == 0:
        partes_do_corpo[0] = '|'  # forca vazia
    elif erro == 1:
        partes_do_corpo[1] = 'O'  # cabeça
    elif erro == 2:
        partes_do_corpo[2] = '|'  # peito
    elif erro == 3:
        partes_do_corpo[3] = '|'  # quadril
    elif erro == 4:
        partes_do_corpo[4] = '/'  # perna esquerda
    elif erro == 5:
        partes_do_corpo[5] = ' \\'  # perna direita
    elif erro == 6:
        partes_do_corpo[6] = '/'  # braço esquerdo
    elif erro == 7:
        partes_do_corpo[7] = '\\'  # braço direito
    print((center - 4) * ' ' + '   ____ ')
    print((center - 4) * ' ' + '  /    ' + partes_do_corpo[0])
    print((center - 4) * ' ' + ' /     ' + partes_do_corpo[1])
    print((center - 4) * ' ' + '|     ' + partes_do_corpo[6] + partes_do_corpo[2] + partes_do_corpo[7])
    print((center - 4) * ' ' + '|      ' + partes_do_corpo[3])
    print((center - 4) * ' ' + '|     ' + partes_do_corpo[4] + partes_do_corpo[5])
    print((center - 4) * ' ' + '|\n')


def atualiza_tela():
    """Esta função é responsável por atualizar a tela a cada comando introduzido pelo usuário
     com as informações úteis ao jogo durante uma partida, tais como: o nome do jogo, nome do
     jogador, número de partidas, número de vitórias, número de derrotas, mostrar as letras
     utilizadas pelo usuário a cada partida, pelo desenho da forca de acordo com a sua evolução,
     e por mostrar as letras encontradas quando elas são descobertas pelo usuário!"""
    limpa_tela()
    print('=' * 100)
    print((center - 4) * ' ' + emojize(':dizzy_face: <<<JOGO DA FORCA: TITAN GAMES>>> :dizzy_face:', use_aliases=True))
    print('=' * 100)
    print((center - 4) * ' ' + f'JOGADOR: {jogador}')
    print((center - 4) * ' ' + f'VITÓRIAS: {vitoria}')
    print((center - 4) * ' ' + f'DERROTAS: {derrota}')
    print((center - 4) * ' ' + f'PARTIDAS: {partidas}')
    print('=' * 100 + '\n')
    mostra_letras_usadas()
    forca()
    print((center - 4) * ' ' + f'A DICA É: {dica}\n')
    mostra_letras_encontradas()
    print()


def jogo_perdido():
    """Esta função é responsável por imprimir na tela uma
    mensagem ao usuário quando ele perde uma partida!"""
    print('=' * 100 + '\n')
    print(
        (center - 4) * ' ' + emojize(f'QUE PENA {jogador}, VOCÊ PERDEU! :skull: :boom: :thumbsdown:', use_aliases=True))
    print((center - 4) * ' ' + f'A PALAVRA ERA: {palavra}' + '\n')
    print((center + 5) * ' ' + '   ____     ')
    print((center + 5) * ' ' + '  /   |     ')
    print((center + 5) * ' ' + ' /    O     ')
    print((center + 5) * ' ' + '|    /|\\   ')
    print((center + 5) * ' ' + '|     |     ')
    print((center + 5) * ' ' + '|    / \\   ')
    print((center + 5) * ' ' + '|           ')
    print((center + 5) * ' ' + '|________\n')
    print('=' * 100 + '\n')
    print('\n' * 5)


def jogo_ganho():
    """Esta função é responsável por imprimir na tela uma
       mensagem ao usuário quando ele ganha uma partida!"""
    print('=' * 100 + '\n')
    print((center - 4) * ' ' + emojize(f'PARABÉNS {jogador}, VOCÊ GANHOU! :sunglasses: :trophy: :thumbsup:',
                                       use_aliases=True))
    print((center - 4) * ' ' + f'A PALAVRA ERA: {palavra}' + '\n')
    print((center - 2) * ' ' + "       ___________      ")
    print((center - 2) * ' ' + "      '._==_==_=_.'     ")
    print((center - 2) * ' ' + "      .-\\:      /-.    ")
    print((center - 2) * ' ' + "     | (|:.     |) |    ")
    print((center - 2) * ' ' + "      '-|:.     |-'     ")
    print((center - 2) * ' ' + "        \\::.    /      ")
    print((center - 2) * ' ' + "         '::. .'        ")
    print((center - 2) * ' ' + "           ) (          ")
    print((center - 2) * ' ' + "         _.' '._        ")
    print((center - 2) * ' ' + "        '-------'       ")
    print()
    print('=' * 100 + '\n')
    print('\n' * 5)


def continuar():
    """Esta função permite o usuário decidir ao final de
    cada partida se deseja continuar jogando ou não!"""
    while True:
        cont = str(input((center - 8) * ' ' + 'DESEJA CONTINUAR JOGANDO? [S] SIM [N] NÃO: ')).upper().strip()
        if cont in 'SN':
            break
        print((center - 8) * ' ' + 'RESPONDA APENAS S PARA SIM OU N PARA NÃO!')
    if cont == 'N':
        limpa_tela()
        print((center - 10) * ' ' + 'OBRIGADO POR JOGAR A FORCA: TITAN GAMES!')
        print((center + 2) * ' ' + emojize('VOLTE SEMPRE!:thumbsup:\n', use_aliases=True))
        print('\n' * 12)
        tempo_final()
        exit()


def tela_reabertura():
    """Esta função é responsável por criar uma tela de reabertura após o usuário decidir continuar no jogo
    ao término de uma partida. Contendo informações úteis, como: nome do jogo, nome do jogador, quantidade
    de partidas disputadas, quantidades de vitórias e quantidade de derrotas!"""
    limpa_tela()
    print('=' * 100)
    print((center - 4) * ' ' + emojize(':dizzy_face: <<<JOGO DA FORCA: TITAN GAMES>>> :dizzy_face:', use_aliases=True))
    print('=' * 100)
    print((center - 4) * ' ' + f'JOGADOR: {jogador}')
    print((center - 4) * ' ' + f'VITÓRIAS: {vitoria}')
    print((center - 4) * ' ' + f'DERROTAS: {derrota}')
    print((center - 4) * ' ' + f'PARTIDAS: {partidas}')
    print('=' * 100 + '\n')
    print('\n' * 10)
    print('=' * 100)


######################### Código principal! ##########################


partidas = 0
vitoria = 0
derrota = 0
erro = 0
center = 30
aux = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
partes_do_corpo = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
letras_usadas = ''
palavra = 0

print('=' * 115)
print((center - 4) * ' ' + emojize(':dizzy_face: <<<BEM VINDO AO JOGO DA FORCA: TITAN GAMES>>> :dizzy_face:',
                                   use_aliases=True))
print('=' * 115 + '\n')
print((
              center - 20) * ' ' + 'ESSE JOGO FOI PRODUZIDO UTILIZANDO A LINGUAGEM DE PROGRAMAÇÃO PYTHON 3.8 (IDE:PYCHARM / UTF-8)\n')
print((
              center - 20) * ' ' + 'DICA 1: MAXIMIZE AO MÁXIMO A TELA QUANDO FOR EXECUTAR O CÓDIGO PARA O ENQUADRAMENTO CORRETO DO JOGO!\n')
print(
    (center - 20) * ' ' + 'DICA 2: NÃO FORAM UTILIZADAS PALAVRAS COMPOSTAS NO JOGO AFIM DE FACILITAR A JOGABILIDADE!\n')
print('=' * 115 + '\n')

jogador = str(input((center - 4) * ' ' + 'QUAL O SEU NOME DE JOGADOR? ')).strip().upper()
print()
print((center - 4) * ' ' + emojize(f'SEJA BEM VINDO {jogador}, BOA SORTE!!! :thumbsup:', use_aliases=True) + '\n')
print('=' * 115 + '\n')

tempo()

while True:

    print((center - 4) * ' ' + 'ESCOLHA UM TEMA:\n')
    print((center - 4) * ' ' + '[1] ANIMAL')
    print((center - 4) * ' ' + '[2] COR')
    print((center - 4) * ' ' + '[3] FRUTA')
    print((center - 4) * ' ' + '[4] TIME')
    print((center - 4) * ' ' + '[5] SAIR\n')

    while True:

        dica = str(input((center - 4) * ' ' + 'OPÇÃO: ')).strip()
        print()
        if dica in '12345':
            break
        print((center - 4) * ' ' + 'RESPONDA APENAS 1, 2, 3, 4 OU 5, DE ACORDO COM A OPÇÃO ESCOLHIDA!\n')

    if dica == '5':
        dica = 'SAIR'
        limpa_tela()
        print((center - 10) * ' ' + 'OBRIGADO POR JOGAR A FORCA: TITAN GAMES!')
        print((center + 2) * ' ' + emojize('VOLTE SEMPRE!:thumbsup:\n', use_aliases=True))
        print('\n' * 12)
        tempo_final()
        exit()

    elif dica == '1':
        dica = 'ANIMAL'
        sorteia = choice
        x = open('animal.txt', 'r')
        lista = x.readlines()
        x.close()
        palavra = sorteia(lista).split('\n')[0].upper()

    elif dica == '2':
        dica = 'COR'
        sorteia = choice
        y = open('cor.txt', 'r')
        lista = y.readlines()
        y.close()
        palavra = sorteia(lista).split('\n')[0].upper()

    elif dica == '3':
        dica = 'FRUTA'
        sorteia = choice
        w = open('fruta.txt', 'r')
        lista = w.readlines()
        w.close()
        palavra = sorteia(lista).split('\n')[0].upper()

    else:
        dica = 'TIME'
        sorteia = choice
        z = open('time.txt', 'r')
        lista = z.readlines()
        z.close()
        palavra = sorteia(lista).split('\n')[0].upper()

    letras_encontradas = '_' * len(palavra)

    atualiza_tela()

    while letras_encontradas != palavra and erro < 7:

        try:
            letra = str(input((center - 4) * ' ' + 'LETRA: ')).upper().strip()

        except:
            letra = ''

        if letra not in letras_usadas and letra in aux:
            letras_usadas += letra + ', '
            if letra in palavra:
                letras_encontradas = muda_letra()
            else:
                erro += 1

        atualiza_tela()

    limpa_tela()

    if erro == 7:
        derrota += 1
        jogo_perdido()

    else:
        vitoria += 1
        jogo_ganho()

    partidas = vitoria + derrota

    tempo()

    continuar()

    tela_reabertura()

    letras_usadas = ''

    partes_do_corpo = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    erro = 0
