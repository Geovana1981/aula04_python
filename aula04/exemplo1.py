# Verificação de Idade

# idade = int(input("Informe sua idade:"))

# if idade  >= 18:
#     print("Você é maior de idade.")

# else:
#     print("Você é menor de idade.") 

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
# Nivelamento com pontos

# pontos = int(input("Quantos pontos? "))

# if pontos >= 100:
#     print("Nível Máximo!")

# elif pontos >= 50:
#     print("Nível Bom!")

# elif pontos >= 25:
#     print("Nível Mediano")

# else:
#     print("Pontuação Baixa. Por favor, tente novamente.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
# Verificação de Login

# usuario = input("Informe o usuário:").lower()
# senha = input("Digite a senha:")

# print(usuario)

# if usuario == 'admin' and senha == '1234':
#     print("Login concluído sucesso")

# else:
#     print("O usuário e/ou a senha estão incorretos. Tente novamente.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
# Condição para brinde

# compra = float(input("Valor da compra:"))
# cliente = input("Você é um cliente frequente? [S/N] ").lower()

# if compra >= 1000 or cliente == "s":
#     print("Parabéns, você está apto à receber o brinde!")

# else:
#     print("Que pena, você não está apto à receber o brinde.")

#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#Aprovação (Nota/Frequência)

# nota = float(input("Informe sua nota:"))
# frequencia = float(input("Informe sua frequência:"))

# if nota >= 7:
#     if frequencia >= 75:
#         print("Aprovado(a)!")
#     else:
#         print("Boa nota, porém está reprovado(a) por falta.")
# else:
#     print("Reprovado (a) por nota.")