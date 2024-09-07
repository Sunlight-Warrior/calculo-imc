nome= input("Digite o nome: ")
cpf= int(input("Digite o CPF: "))
renda= float(input("Digite sua renda: "))
if renda <= 1903.98:
    aliquota = "Isento"
elif renda <= 2826.65:
    aliquota = "7.5%"
elif renda <= 3751.05:
    aliquota = "15%"
elif renda <= 4664.68:
    aliquota = "22.5%"
else:
    aliquota = "27.5%"
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Renda: {renda}")
print(f"Alíquota: {aliquota}")
