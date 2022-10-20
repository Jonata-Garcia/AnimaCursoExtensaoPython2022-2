# Meu primeiro projeto Python !!!
#
# print() = comando saida
print("Hello Word !!!")

# Quando quiser guardar uma String
nome ="Jonata Garcia"
#Quando quiser gaudar um número inteiro
idade =20

# Exibir o meu nome ( que está dentro da variávelo nome)
print(nome)
print(idade)

#Quando quiser exibir a frase "Minha idade é " completando com o conteúdo da variável idade    (3 maneiras)
print("Minha idade é " +str(idade)+ " anos")
print(f"Minha idade é {idade} anos\n")
print("Minha idade é {} anos\n".format(idade))

# Quando quiser exibir "Meu nome é... e tenho... anos..." trocando pelas variáveis nome e idade
print("Meu nome é {} e tenho {} anos".format(nome,idade))