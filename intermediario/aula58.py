salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


novo_salario = salario_bonus(500)  # 2500
print(f" o seu salário bonus é de : {novo_salario}")