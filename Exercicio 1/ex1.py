print('Bem-vindo a Loja do Kaike Santos Rocha!')
#Recebendo a entrada do valor do produto e da quantidade
valor_prod = float(input('Digite o valor do produto: '))
quant_prod  = float(input('Digite a quantidade do produto: '))

#verificando se a quantidade do produto é menor que 200
if(quant_prod < 200):
    print('O valor do produto SEM desconto: R$ {}' .format(valor_prod))
    print('O valor do produto COM desconto: R$: {}' .format(valor_prod))

#verificando se a quantidade do produto e maior ou igual a 200 e menor que 1000
elif(quant_prod >= 200 and quant_prod < 1000):
    #obtendo o valor final com o desconto de 5%
    valor_final = valor_prod - (valor_prod*0.05)
    print('O valor do produto SEM desconto: R$ {}' .format(valor_prod))
    print('O valor do produto COM desconto: R$: {}' .format(valor_final))
#verificando se a quantidade do produto é maior ou igual a 1000 e menor que 2000
elif(quant_prod >= 1000 and quant_prod < 2000):
    #obtendo o valor final com o desconto de 10%
    valor_final = valor_prod - (valor_prod*0.10)
    print('O valor do produto SEM desconto: R$ {}' .format(valor_prod))
    print('O valor do produto COM desconto: R$: {}' .format(valor_final))
else:
    valor_final = valor_prod - (valor_prod*0.20)
    #obtendo o valor final com o desconto de 20%
    print('O valor do produto SEM desconto: R$ {}' .format(valor_prod))
    print('O valor do produto COM desconto: R$: {}' .format(valor_final))