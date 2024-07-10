#Lista de tarefas
lista = []

#Função cadastrar uma nova tarefa a lista
def cadastrar_tarefa(tarefa):
    if tarefa not in lista:
        lista.append(tarefa)
        print(f'Tarefa "{tarefa}" foi adicionada com sucesso!')
    else:
        print(f'Tarefa "{tarefa}" já está adicionada.')

#Função remover uma tarefa da lista
def remover_tarefa(tarefa):
    if tarefa in lista:
        lista.remove(tarefa)
        print(f'Tarefa "{tarefa}" foi removida com sucesso!')
    else:
        print(f'Tarefa "{tarefa}" não encontrada.')

#Função para alterar uma tarefa da lista
def modificar_tarefa(tarefa_antiga, tarefa_nova):
    if tarefa_antiga in lista:
        indice = lista.index(tarefa_antiga)
        lista[indice] = tarefa_nova
        print(f'Tarefa "{tarefa_antiga}" foi modificada para "{tarefa_nova}" com sucesso!')
    else:
        print(f'Tarefa "{tarefa_antiga}" não encontrada')


#Loop do sistema
while True:
    print('\nDigite o numero 1 para adicionar mais uma tarefa.')
    print('Digite o numero 2 para remover uma tarefa.')
    print('Digite o numero 3 para modificar uma tarefa.')
    print('Digite o numero 4 para ver a lista de tarefas.')
    print('Digite o numero 0 para sair.')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        for tarefa in lista:
            print(f'- {tarefa}')
        tarefa = (input('Digite a tarefa a ser adicionada: '))
        cadastrar_tarefa(tarefa)
    elif escolha == '2':
        print('Lista de Tarefas:')
        for tarefa in lista:
            print(f'- {tarefa}')
        tarefa = (input('Digite a tarefa a ser removida: '))
        remover_tarefa(tarefa)
    elif escolha == '3':
        print('Lista de tarefas:')
        for tarefa in lista:
            print(f'- {tarefa}')
        tarefa_antiga = input('Digite a tarefa que deseja ser modificada: ')
        tarefa_nova = input('Digite a nova descrição da tarefa: ')
        modificar_tarefa(tarefa_antiga, tarefa_nova)
    elif escolha == '4':
        print('Lista de tarefas:')
        for tarefa in lista:
            print(f'- {tarefa}')
    elif escolha == '0':
        print('Saindo do sistema...')
        break
    else:
        print('Opção invalida. Por favor, tente novamente.')