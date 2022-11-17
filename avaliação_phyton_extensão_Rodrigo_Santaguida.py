print("Olá, seja Bem Vindo ao meu código")

print('Bora lá, hoje iremos calcular o seu IMC, para que possamos caluclar o seu IMC, precisaremos de suas informações por gentileza:')

print('Obs: Colocar os valores de ALTURA e PESO com ponto')

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2
  
print("Seu IMC é: %.4f" % imc)
 
if imc < 16:
	print("Classificação = Magreza grave")
elif imc < 17:
	print("Classificação = Magreza moderada")
elif imc < 18.5:
	print("Classificação = Magreza leve")
elif imc < 25:
	print("Classificação = Saudável")
elif imc < 30:
	print("Classificação = Sobrepeso")
elif imc < 35:
	print("Classificação = Obesidade Grau I")
elif imc < 40:
	print("Classificação = Obesidade Grau II (severa)")
else:
	print("Classificação = Obesidade Grau III (mórbida)")