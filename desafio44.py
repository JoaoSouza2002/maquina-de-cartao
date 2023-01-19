price = 100
descount = 0
options = ["1 - Dinheiro/Cheque","2 - Avista no cartão", "3 - 3x ou mais no cartão", "4 - 2x no cartão"]
for option in options:
    print(option)
value = input('Qual opção deseja?\n')
match value:
    case '1':
        descount = 0.10
    case '2':
        descount = 0.05
    case'3':
        descount = 0.20
    case '4':
        descount = 0
    case _:
        print('Essa não é uma opção')
        quit()
print(f'\fvocê escolheu a forma de pagamento: {option}\n com o desconto: {price*descount}\n o valor total a ser pago é de: {(price - price*descount)}')

