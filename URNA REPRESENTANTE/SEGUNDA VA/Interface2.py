arquivo = open('alunos.txt','r')
votos = {}
cadastrado = 1

count = 0
for cpf in arquivo:
    if count%2==1:
        votos[cpf[:-1]] = 0
    count+=1

arquivo.close()
arquivo = open('alunos.txt','r')

while True:
    print ('''\n\nESCOLHA UMA DAS OPÇÕES ABAIXO:
[1] LIBERAR VOTAÇÃO.
[2] APURAÇÃO.
[3] ENCERRAR PROGRAMA. ''')

    ESCOLHA = input()

    if ESCOLHA == '1':
        print ('DIGITE O SEU CPF: ')

        cpf_de_qm_vota = input()

        encontrou = False

        count = 0
        for linha in arquivo:
            if count%2==0:
                nome = linha[:-1]
            else:
                cpf = linha[:-1]
                if cpf == cpf_de_qm_vota:
                    print ('NOME/CPF')
                    print (nome, cpf)
                    encontrou = True
                    break
            count += 1

            if cpf_de_qm_vota == linha[:-1]:
                encontrou = True
                break
        if encontrou == True:
            print('\nCONFIRMADO.\n')
            voto = input ('EM QUEM DESEJA VOTAR? ')
            votos[voto] += 1
            print('VOTO CONFIRMADO')


        else:
            print ('\nCPF NÃO ENCONTRADO\n')

    if ESCOLHA == '2':
        print(votos)

    if ESCOLHA == '3':
        print ('FIM DO PROGRAMA.')
        break

