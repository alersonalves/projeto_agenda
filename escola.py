from utils import menu
from manipulaAluno import cadastrar, listar, buscar, alterar, excluir, naoEncontrado

turma = []

while True:
    menu()
    opcao = int (input ("Selecione a opção: "))

    if opcao == 1:
        while True:
            cadastrar(turma)
            continuar = input ("Deseja continuar? (S / N) ")
            if continuar == 'N':
                break

    elif opcao == 2:
        listar(turma)

    elif opcao == 3:
        posicao = buscar(turma)
        if posicao == -1:
            naoEncontrado()
    
    elif opcao == 4:
        posicao = buscar(turma)
        if posicao >= 0:
           alterar(posicao, turma)
        else:
            naoEncontrado()

    elif opcao == 5:
        posicao = buscar(turma)
        if posicao >= 0:
           excluir(posicao, turma)
        else:
            naoEncontrado()   

    elif opcao == 9:
        break     
