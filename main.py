Setor = []
cont = 1
NomeSetor = ""

print("=============Matrizes de salarios entre setores=============")
for linha in range (3):
	Salario = []
	if cont == 1:
		NomeSetor = "RH"
	elif cont == 2:
		NomeSetor = "TI"
	else:
		NomeSetor = "Marketing"
	cont += 1 

	print("Setor de",NomeSetor )
	for coluna in range (5):
		print("Informe o salário do",coluna+1,"° Funcionario.")
		valor = input()
		Salario.append(valor)
	Setor.append(Salario)

cont = 1
NomeSetor = ""


for Salario in Setor:
	if cont == 1:
		NomeSetor = "RH"
	elif cont == 2:
		NomeSetor = "TI"
	else:
		NomeSetor = "Marketing"
	cont += 1

	print("Salarios do Setor de",NomeSetor)
	for valor in Salario:
		print(valor)
	print("______________________________________________________")


#soma dos salarios
SomaTI = 0
SomaRH = 0
SomaMK = 0
SomaSetor = 0

cont = 1


for Salario in Setor:
	for valor in Salario:
		SomaSetor = SomaSetor + int(valor)
		
	if cont == 1:
		SomaRH = SomaSetor
	elif cont == 2:
		SomaTI = SomaSetor
	else:
		SomaMK = SomaSetor

	cont += 1
	SomaSetor = 0

print("A soma dos salarios do setor de RH foi de:R$",SomaRH)
print("A soma dos salarios do setor de TI foi de:R$",SomaTI)
print("A soma dos salarios do setor de MK foi de:R$",SomaMK)






