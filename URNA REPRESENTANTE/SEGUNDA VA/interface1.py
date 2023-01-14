while True:
        print ('OLÁ,SEJA BEM-VINDO(A)!')
        print ('ESCOLHA UMA DAS OPÇÕES ABAIXO:')
        print ('[1] CADASTRO.')
        print ('[2] SAIR.')
        ESCOLHA = input ()

        if ESCOLHA == '2':
            print ('PROGRAMA ENCERRADO.')
            break

        if ESCOLHA == '1':
            NOM = input ('DIGITE SEU NOME:')
            CPF = input ('DIGITE SEU CPF |APENAS NÚMEROS!|:')

            LINHA1 = [NOM]
            LINHA2 = [CPF]

            if len(CPF) == 11:
                with open('alunos.txt','a') as arquivo:
                    for NOME in LINHA1:
                        arquivo.write (NOM)
                        arquivo.write ('\n' )

                    for CPF in  LINHA2:
                        arquivo.write (CPF)
                        arquivo.write ('\n')
                    print ( "\n\nOLÁ {}\nCONFIRMADO PARA VOTAÇÃO!\n".format (LINHA1[0]))

            elif len(CPF) != 11:
                print ( '-' * 30)
                print ('\nCPF INVÁLIDO!\n')
                print ('-' * 30)









