from random import randint
numero = str(randint(100000000, 999999999))  # gera um número aleatório entre os dois parâmetros

novo_cpf = numero  # recebe o número aleatório gerado pela função acima (9 numeros no total)
reverso = 10  # contador reverso
total = 0  # total de multiplicações

for index in range(19):
    if index > 8:  # primeiro índice vai de 0 até 9
        index -= 9  # os 9 primeiros dígitos do CPF

    total += int(novo_cpf[index]) * reverso  # valor total da multiplicação

    reverso -= 1  # decrementa o valor reverso
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:  # se o dígito for maior que 9 o valor será 0
            digito = 0
        total = 0  #zera o total
        novo_cpf += str(digito)  # concatena o dígito zerado ao novo CPF
print(f'CPF GERADO: {novo_cpf}')
