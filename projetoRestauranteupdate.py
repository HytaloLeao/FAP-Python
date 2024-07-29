# Projetos de Lógica de Programação com Python

# Para cada objeto criar no mínimo dois dados.

# Exemplo: Médico(nome, crm), Pacientes(nome, cpf)
# 
# # O sistema deverá realizar operações de CRUD com programação estruturada.

# O projeto deve ser colocado no GitHub.

# No dia ? será realizado um sorteio para definir a apresentação dos projetos.

# Restaurante e Pedidos
# - Descrição: Um restaurante recebe vários pedidos. Cada
# pedido é feito por um cliente específico no restaurante.
# - Relação: Um restaurante -> Muitos pedidos

restaurantes = []
pedidos = []
prox_id_pedido = 1

#Funções para CRUD

def criar_restaurantes(nome, localizacao, tipo_cozinha):
    restaurante = {
        'nome': nome,
        'localização': localizacao,
        'tipo_cozinha': tipo_cozinha
    }
    restaurantes.append(restaurante)
    return restaurantes

def listar_restaurantes():
    print('Lista de Restaurantes:')
    for restaurante in restaurantes:
        print(f'Nome: {restaurante["nome"]}, Localização: {restaurante["localizacao"]}, Tipo de cozinha: {restaurante["tipo_cozinha"]}')

def atualizar_restaurante(nome_antigo, nome_novo, localizacao_nova, tipo_cozinha_nova):
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_antigo:
            restaurante['nome'] = nome_novo
            restaurante['localizacao'] = localizacao_nova
            restaurante['tipo_cozinha'] = tipo_cozinha_nova
            return True
        
def excluir_restaurante(nome):
    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            restaurante.remove(restaurante)
            return True
    return False

def criar_pedido(cliente, itens):
    global prox_id_pedido
    pedido = {
        'numero_pedido': prox_id_pedido,
        'cliente': cliente,
        'itens': itens,
        'status': 'Em andamento'
    }
    prox_id_pedido += 1
    pedidos.append(pedido)
    return pedido

def listar_pedido():
    print('Lista de Restaurante:')
    for pedido in pedidos:
        print(f'Numero do pedido: {pedido["numero_pedido"]}, Cliente: {pedido["cliente"]}, Itens: {pedido{"itens"}}, Status: {pedido["status"]}')

def atualizar_pedido(pedido_antigo, pedido_novo)
    for pedido in pedidos:
        if pedido['itens'] == pedido_antigo:
            pedido['itens'] == pedido_novo
            return True
        
def excluir_pedido(numero_pedido):
    for pedido in pedidos:
        if pedido['numero_pedido'] == numero_pedido:
            pedido.remove(pedido)
            return True
    return False

#Loop do Sistema (MENU)

while True:
    print('\n (1) Criar restaurante.')
    print('(2) Modificar restaurante.')
    print('(3) Excluir restaurante.')
    print('(4) Listar restaurante.')
    print('======================================')
    print('(5) Criar pedido.')
    print('(6) Modificar o pedido.')
    print('(7) Excluir o pedido.')
    print('(8) Listar os pedidos.')

    escolha = input('Escolha sua opção: ')

    if escolha == 1:
        for restaurante in restaurantes
        nome = (input('Digite o nome do restaurante: '))
        localizacao = (input('Digite a localização do seu restaurante: '))
        tipo_cozinha = input('Digite o tipo da cozinha: ')
        criar_restaurantes(nome, localizacao, tipo_cozinha)