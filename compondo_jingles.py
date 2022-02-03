notas_dicio = {'w' : 1,
'h' : 1/2,
'q' : 1/4,
'e' : 1/8,
's' : 1/16,
't' : 1/32,               
'x' : 1/64} #Mapeamento dos identificadores e suas durações..

startup = 1
soma = 0
soma_compasso = 0
divisoes = 0
qntde_corretos = 0
errado = ''
lista_errados = []

while startup != 0:
    entrada_user = input('Entre com a composição: ') #Proteção para o usuário não digitar números e outros caracteres.
    input_user_std = entrada_user.lower() #Proteção, caso o usuário entre com letras maiúsculas

    #name = gifts_dicio.get(input_user_std) #Resgatando o valor no dicionário.
    lista_string_original = list(input_user_std) #Colocando string em lista para manipulação.
    
    for item in lista_string_original:
        #print(f"Os itens percorridos, são: {item}") #Debug in Jupyter Notebook.
        if item != '/':
            duracao = notas_dicio[item]
            soma_compasso = soma_compasso + duracao
            errado = errado + item #Adiciona as letras em uma string que será mostrada, caso o compasso não seja 1
        
        elif item == '/': # Se item da lista atual for uma barra.
            if soma_compasso == 1: #Se o compasso for 1, está tudo certo.
                qntde_corretos = qntde_corretos + 1 #soma os corretos
                errado = '' #Zera a string que coleta os errados.
                
            elif (soma_compasso != 1) and (errado != ''): #Se o compasso estiver errado e não for a primeira barra.
                lista_errados.append(errado.upper()) #Coloca em uma lista, tudo maiúculo, o que foi coletado na string errado.
                errado = '' #Zera a string que coleta os errados.
                
            soma_compasso = 0 #Zera a variável soma_compasso para verificação de novo intervalo.
    
    #print(f"A soma_compasso é: {soma_compasso}")

    print(f"Qtd. de Corretos: {qntde_corretos}")
    
    if len(lista_errados) > 0:
        print(f"Incorretos: {lista_errados}")
    
    startup = int(input('Digite 1, para testar presente novamente.\nDigite 0, para sair\n')) # Menu usuário
    
    soma = 0
    qntde_corretos = 0
    del lista_errados
    entrada_user = ''
    input_user_std = ''
    lista_errados = []
print("\nAté mais")