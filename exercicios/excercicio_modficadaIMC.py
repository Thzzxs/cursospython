nome_exercicio = "calculadora de imc basica"

nome = "Thiago"
altura = 1.80
peso= 95
imc = peso/(altura*altura)

""" f string; :.2f - casas decimais"""
print(nome_exercicio)
linha_1 = f"{nome} tem {altura:.2f} de altura"
print(linha_1)
linha_2 =f"{nome} pesa  {peso} e seu imc é  {imc:.2f}"
print(linha_2)