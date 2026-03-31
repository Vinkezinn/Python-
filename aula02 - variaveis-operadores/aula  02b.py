from sqlalchemy.sql.operators import truediv

n1=5
n2=2

print(type(n1)), type(n1)

result= n1//n2
print(result,type(result))

#operadores de atribuição
n=15
print()#pular uma linha
print(n)

n=n + 2#acumulador
print(n)

n-=2
print(n)

#operadores relacionais
print()
print(6<2)

idade=21
print(idade == 21)

logado=True
print(logado, type(logado))

maior_idade= idade>18
print(maior_idade, type(maior_idade))

#stings
nome1="Marcos"
nome2="marcos"

print(nome1.upper() == nome2.upper())


