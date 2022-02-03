def super_digito(numero_p):
    soma = 0
    p_list = list(numero_p)
    #print(f"A lista p: {p_list}\n") #Debug program in Jupyter Notebook
    
    tamanho = len(p_list)
    if tamanho > 1:
        for i in range(tamanho):
            soma = soma + int(p_list[i])
        #print(f"A soma é: {soma}\n") #Debug program in Jupyter Notebook
        
        next_call = str(soma)
        roberto = super_digito(next_call)
        #print(f"O roberto vale: {roberto}\n") #Debug program in Jupyter Notebook
    else:
        soma = int(p_list[0])
        #print(f"A soma else: {soma}\n") #Debug program in Jupyter Notebook
        print(f"O super dígito é: {soma}\n") #Debug program in Jupyter Notebook
        return soma
        #return p_list[0]

#-------------------------------------------------------------------------------------------------#
#Função main:
execution = 1 #Varíavel que inicializa execução.
#jogadores = []
while execution != 0:
    lista_numeros = []
    lista_original = []
    execution = int(input('Digite 1, para cálculo do super dígito.\nDigite 0, para SAIR:\n')) # Menu usuário
    if execution != 0:
        n_number = input('Entre como o número "n": \n') # Menu usuário
        k_number = int(input('Entre como o número "k": \n')) # Menu usuário
        
        p_number = n_number*k_number
        print(f"Número p: {p_number}\n") #Debug program in Jupyter Notebook
        
        recursive_sum = super_digito(p_number)
        
        #p_list = list(p_number)
        #print(f"O resultado da soma recursiva é: {super_digito(p_number)}\n") #Debug program in Jupyter Notebook