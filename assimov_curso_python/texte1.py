#Solicita o nome do usuário
nome = input("Seu nome ")
#Solicita a idade do usuário
idade = int(input("Sua idade "))

n = str(len(nome))

#Sauda o usário em seguida  diz quantas letras seu nome tem e finalmente diz qual será sua idade daqui 5 anos
print("Hello, " + nome + "!")

print("Seu nome tem " + n + " letras")

print("Daqui 5 anos você terá " + str((5 + idade)))