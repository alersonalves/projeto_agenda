turma = []

while True:
    opcao = int (input ("Selecione a opção: 1 - Cadastrar / 2 - Listar / 3 - Pesquisar / 4 - Alterar / 5 - Excluir / 9 - Sair: "))

    if opcao == 1:
        while True:
            aluno = {}
            aluno['nome'] = input ("Informe o nome do aluno: ")
            aluno['disciplina'] = input ("Informe a disciplina: ")
            aluno['nota1'] = float (input ("Informe a nota 1: "))
            aluno['nota2'] = float (input ("Informe a nota 2: "))
            aluno['nota3'] = float (input ("Informe a nota 3: "))
            aluno['nota4'] = float (input ("Informe a nota 4: "))
            turma.append(aluno)
            continuar = input ("Deseja continuar? (S / N) ")
            if continuar == 'N':
                break

    elif opcao == 2:
        for i in turma:
            print (i)
            media = (i['nota1'] + i['nota2'] + i['nota3'] + i['nota4']) / 4
            if media >= 7:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"
            print (f'Média: {media} / Situação: {situacao}')

    elif opcao == 3:
        pesquisa = input ("Informe o nome do aluno para a pesquisa: ")
        encontrou = 0
        for i in turma:
            if i['nome'] == pesquisa:
                print (i)
                encontrou = 1
        if encontrou == 0:
            print ("Aluno não encontrado.")
    
    elif opcao == 4:
        posicao = 0
        encontrou = 0
        pesquisa = input ("Informe o nome do aluno para a alteração: ")
        for i in turma:
            if i['nome'] == pesquisa:
                print (i)
                posicao = i
                encontrou = 1
                while True:
                    dado = input ("Qual o dado você deseja alterar? ")
                    if dado == 'nome' or dado == 'disciplina':
                        valor = input (f"Informe o novo valor para {dado}: ")
                    else:
                        valor = float (input (f"Informe o novo valor para {dado}: "))
                    posicao[dado] = valor
                    print (posicao)
                    continuar = input ("Deseja alterar outro dado? (S / N) ")
                    if continuar == 'N':
                        break

        if encontrou == 0:
            print ("Aluno não encontrado.")

        
    elif opcao == 5:
        posicao = 0
        while True:
            pesquisa = input ("Informe o nome do aluno para a exclusão: ")
            for i in turma:
                if i['nome'] == pesquisa:
                    print (i)
                    posicao = i
            if posicao != 0:
                deleta = input (f"Deseja realmente excluir os dados de {pesquisa}? (S / N) ")
                if deleta == 'S':
                    turma.remove(posicao)
                    print (f"Aluno(a) {pesquisa} excluído(a) da base de dados.")
            else:
                print ('Aluno(a) não encontrado(a).')
            continuar = input ("Deseja realizar outra exclusão? (S / N) ")
            if continuar == 'N':
                break       

    elif opcao == 9:
        break     
