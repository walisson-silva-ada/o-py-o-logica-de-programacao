import random

#Função para definir os jogadores
def jogadores():
    numero_de_jogadores = int(input('Quantos jogadores? '))
    maos_jogadores = {}
    jogadores = [(input(f'Nome do jogador {i+1}: ')) for i in range(numero_de_jogadores)]
    for i in jogadores:
        maos_jogadores[i]=[]
    return(maos_jogadores)

#Função para comprar cartas
def comprar_carta():
    carta = (random.randint(0, len(baralho)))
    print(f'\nVocê comprou um {baralho[carta]}')
    adicional = (baralho[carta])
    baralho.pop(carta)
    return adicional

#Função de definir o baralho
def baralho():
    baralho = [i+1 for i in range(10)]*4
    [baralho.append(10) for i in range(12)]
    return baralho

#Definir o vencedor
def vencedor():
    #Excluir os perdedores 
    chance_ganhar=[]
    for i in mao_jogadores:
        if sum(mao_jogadores[i])<=21:
            chance_ganhar.append(i)

    #Selecionar os vencedores
    valores_ganhador=[]
    for i in chance_ganhar:
        valores_ganhador.append(sum(mao_jogadores[i]))
    
    ganhadores=[]
    for i in chance_ganhar:
        if sum(mao_jogadores[i]) == max(valores_ganhador):
            ganhadores.append(i)
    
    if len(ganhadores)==1:
        print(f'O ganhador foi {ganhadores[0]}')
    else:
        print(f'Os ganahadores foram {ganhadores}')
        

#    indice_vencedor= ganhador.index(max(ganhador))
#    print(f'O vencedor é {chance_ganhar[indice_vencedor]}')



#Chamada das funções
baralho = baralho()
mao_jogadores=jogadores()

#Main
for i in mao_jogadores:
    comando = '1'  
    print(f'\nTurno do jogador(a): {i}')
    while comando !='2':
        print('\n1.Comprar 2.Parar')
        comando = input('Digite o comando: ')
        if sum(mao_jogadores[i]) == 21:
            print('Você chegou no valor máximo do jogo!')
            comando = '2'
        elif sum(mao_jogadores[i]) >21:
            print('Você perdeu o jogo!')
            comando = '2'
        elif comando == '1':
            carta = comprar_carta()
            print(carta)
            mao_jogadores[i].append(carta)
            print(f'Sua mão vale {sum(mao_jogadores[i])}')
        elif comando == '2':
            print(f'Sua mão final é {sum(mao_jogadores[i])}')
        else:
            print('Digite algo válido!')

#Final dos turnos!
print('\nFinal do jogo!\n')

vencedor()
        