feliz_natal = {'brasil'          :'Feliz Natal!',
'alemanha'        :'Frohliche Weihnachten!',
'austria'         :'Frohe Weihnacht!',
'coreia'          :'Chuk Sung Tan!',
'espanha'         :'Feliz Navidad!',
'grecia'          :'Kala Christougena!',
'estados-unidos'  :'Merry Christmas!',
'inglaterra'      :'Merry Christmas!',
'australia'       :'Merry Christmas!',
'portugal'        :'Feliz Natal!',
'suecia'          :'God Jul!',
'turquia'         :'Mutlu Noeller',
'argentina'       :'Feliz Navidad!',
'chile'           :'Feliz Navidad!',
'mexico'          :'Feliz Navidad!',
'antardida'       :'Merry Christmas!',
'canada'          :'Merry Christmas!',
'irlanda'         :'Nollaig Shona Dhuit!',
'belgica'         :'Zalig Kerstfeest!',
'italia'          :'Buon Natale!',
'libia'           :'Buon Natale!',
'siria'           :'Milad Mubarak!',
'marrocos'        :'Milad Mubarak!',
'japao'           :'Merii Kurisumasu!',}

comando = 0
while comando !=2:
    print('\n1. Para selecionar o pais\n2. Encerrar o programa!')
    comando = int(input('Digite o comando: '))
    if comando == 1:
        pais = input('\nDigite o pais para saber o Feliz Natal: ')
        if (pais in feliz_natal.keys()) == False:
            print('--- NOT FOUND ---')
        else:
            print(feliz_natal[pais])
    elif comando == 2:
        print('\nO programa foi encerado! Ho ho ho')
    else:
        print('\nDigite uma opção válida!')