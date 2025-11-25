valor = float(input("Informe o valor da sua compra:"))

if valor  >= 250.00:
    desconto = valor * 0.16
    total = valor - desconto
    print("Parabéns! Com o seu valor gasto, o desconto de 16% é aplicável. Sendo assim, o total a pagar é de R$", total) 

else:
    print("Infelizmente, com o seu valor gasto, o desconto de 16% não é aplicável. Sendo assim, o total a pagar continua sendo de R$", valor)