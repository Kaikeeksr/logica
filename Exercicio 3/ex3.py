# variaveis globais
lista_colaborador = []
id_global = 0


def cadastrar_colaborador(id_gobal):
    print('-------------------- CADASTRO --------------------')
    print('id do colaborador: {}' .format(id_global))
    nome = input('Digite o NOME do colaborador: ')
    setor = input('Digite o SETOR do colaborador: ')
    pagamento = int(input('Digite o PAGAMENTO do colaborador: R$ '))
    dicionario_colaborador = {'id': id_global,
                              'nome': nome,
                              'setor': setor,
                              'pagamento': pagamento
                              }
    # copiando o dicionario do colaborar pra dentro da lista
    lista_colaborador.append(dicionario_colaborador.copy())
    

def consultar_colaborador():
    print('-------------------- CONSULTA --------------------')
    op_consultar = input('Escolha a opção desejada: \n' +
                         '1 - Consultar todos os colaboradores \n' 
                         '2 - Consultar colaborador por id \n' +
                         '3 - Consultar colaborador(es) por setor \n' +
                         '4 - retornar \n >>')
    if (op_consultar == '1'):
        print('Você escolheu a opção de consultar todos os colaboradores!')
        for colaborador in lista_colaborador:  #varre a lista de colaboradores
            print('------------------------------------------')
            for key, value in colaborador.items(): #varre todos os conjuntos de 'key' 'value' do dicionario colaborador
                print('{}: {}' .format(key, value))
        print('------------------------------------------')
    elif(op_consultar == '2'):
        print('Você escolheu a opção de consultar um colaborador por id!')
        id_desejado = int(input('Digite o id do colaborador(a): '))
        for colaborador in lista_colaborador:
            if colaborador['id'] == id_desejado: #se o id_desejado é igual id dentro da lista
                print('------------------------------------------')
                for key, value in colaborador.items():
                    print('{}: {}' .format(key, value))
            print('------------------------------------------')    
    elif(op_consultar == '3'):
        print('Você escolheu a opção de consultar um colaborador por setor!')
        setor_desejado = (input('Digite o setor do colaborador(a): '))
        for colaborador in lista_colaborador:
            if colaborador['setor'] == setor_desejado: #se o id_desejado é igual id dentro da lista
                print('------------------------------------------')
                for key, value in colaborador.items():    
                    print('{}: {}' .format(key, value))
            print('------------------------------------------')               
    elif(op_consultar == '4'):
        return #sai da função consulta_colaborador() e volta pra main

def remover_colaborador():
    print('-------------------- REMOVER --------------------')
    id_desejado = int(input('Digite o id do colaborador que deseja REMOVER: '))
    for colaborador in lista_colaborador:
        if colaborador['id'] == id_desejado:
            lista_colaborador.remove(colaborador)
            print('Colaborador de id: {} foi removido!' .format(id_desejado))
# main
print('Bem-vindo ao controle de colaboradores do Kaike Santos Rocha!')
print('**********************************************')
print('-------------------- MENU --------------------')
while True:
    op = input('Escolha a opção desejada: \n 1 - Cadastrar colaborador(es) \n 2 - Consultar colaborador(es) \n 3 - Remover colaborador \n 4 - encerrar\n >> ')
    if (op == '1'):
        # toda vez que função for chamada, será adicionadp + 1 ao id_global
        id_global = id_global + 1
        cadastrar_colaborador(id_global)
    elif (op == '2'):
        consultar_colaborador()
    elif (op == '3'):
        remover_colaborador()
    elif (op == '4'):
        break
    else:
        print('Opção inválida!')
        continue
