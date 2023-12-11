def cadastrar (turma):
    aluno = {}
    aluno['nome'] = input ("Informe o nome do aluno: ")
    aluno['disciplina'] = input ("Informe a disciplina: ")
    aluno['nota1'] = float (input ("Informe a nota 1: "))
    aluno['nota2'] = float (input ("Informe a nota 2: "))
    aluno['nota3'] = float (input ("Informe a nota 3: "))
    aluno['nota4'] = float (input ("Informe a nota 4: "))
    turma.append(aluno)

def listar(turma):
    for i in turma:
        print (i)
        media = (i['nota1'] + i['nota2'] + i['nota3'] + i['nota4']) / 4
        if media >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
        print (f'Média: {media} / Situação: {situacao}')

def buscar(turma):
        pesquisa = input ("Informe o nome do aluno: ")
        posicao = -1
        a = 0
        for i in turma:
            if i['nome'] == pesquisa:
                print (i)
                posicao = a
            a = a + 1
        return posicao

def alterar(posicao, turma):
     while True:
        dado = input ("Qual o dado você deseja alterar? ")
        if dado == 'nome' or dado == 'disciplina':
            valor = input (f"Informe o novo valor para {dado}: ")
        else:
            valor = float (input (f"Informe o novo valor para {dado}: "))
        turma[posicao][dado] = valor
        print (posicao)
        continuar = input ("Deseja alterar outro dado? (S / N) ")
        if continuar == 'N':
            break

def excluir(posicao, turma):
    nome = turma[posicao]['nome']
    deleta = input (f"Deseja realmente excluir os dados de {nome}? (S / N) ")
    if deleta == 'S':
        turma.pop(posicao)
        print (f"Aluno(a) {nome} excluído(a) da base de dados.")
    
def naoEncontrado():
    print ("Aluno não encontrado")
