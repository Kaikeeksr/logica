# função cachorro_peso
def cachorro_peso():
    print('-------------------- Etapa 1 - Peso do Cachorro --------------------')
    # laço de repetição
    while True:
        try:
            peso = float(input('Digite o peso do cachorro (KG): '))
            if (peso > 50):
                print('não aceitamos cachorros tão grandes!')
            elif (peso <= 3):
                return 40
            elif (peso >= 3 and peso < 10):
                return 50
            elif (peso >= 10 and peso < 30):
                return 60
            else:
                return 70
        except ValueError:  # tratando o ValueError dentro do except
            print('Por favor, digite um valor númerico!')
            continue  # se cair nessa opção, volte para o início do laço


def cachorro_pelo():
    print('-------------------- Etapa 2 - Pelo do Cachorro --------------------')
    while True:
        pelo_option = input(
            'Selecione o tipo de pelo do cachorro: \n c - curto \n m - médio \n l - longo \n >>')
        pelo_option = pelo_option.upper()  # 'transforma' a string em maiuscula
        pelo_option = pelo_option.strip()  # remove espaços indesejados

        if (pelo_option == 'C'):
            return 1.0
        elif (pelo_option == 'M'):
            return 1.5
        elif (pelo_option == 'L'):
            return 2.0
        else:
            print('Por favor, digite uma das opções válidas!')
            continue  # se cair nessa opção, volte para o início do laço


def cachorro_extra():
    print('-------------------- Etapa 3 - Adicionais --------------------')
    acomulador = 0
    while True:
        adicional = input(
            'Deseja adicionar mais um serviço? \n 0 - Não desejo mais nada \n 1 - Corte de unhas - R$ 10,00 \n 2 - Escovar os dentes - R$ 12,00 \n 3 - Limpeza das orelhas R$ 15,00 \n >>')
        if (adicional == '0'):
            return acomulador
        elif (adicional == '1'):
            acomulador = acomulador + 10.00
            continue
        elif (adicional == '2'):
            acomulador = acomulador + 12.00
            continue
        elif (adicional == '3'):
            acomulador = acomulador + 15.00
        else:
            print('Por favor, digite uma das opções válidas!')
            continue  # se cair nessa opção, volte para o início do laço

# inicio main
print('-------------------- Bem-vindo ao Petshop do Kaike --------------------')
base = cachorro_peso()
multiplicador = cachorro_pelo()
extra = cachorro_extra()

valor_final = base * multiplicador + extra
print('Total a pagar: R$ {:.2f} (peso: R$ {:.2f} * pelo: {} + adicional(is): R$ {:.2f})' .format(
    valor_final, base, multiplicador, extra))
