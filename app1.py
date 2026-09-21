#Recebe o nome do usuário na variável
name = input("Qual seu nome? ")

#Recebe a idade do usuário na variável 
age = input("Qual a sua idade? ") 

# Exibe uma mensagem formatada 
print("Olá", name,"!")
print("Você tem", age, "anos")

# Usando string formatada (f) - Melhor prática.
print()
print(f"Olá {name}! Você tem {age} anos.")