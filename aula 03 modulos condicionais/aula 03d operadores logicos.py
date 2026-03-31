# logica E (and)
from sympy import false

verifica_email= True
verifica_senha= True

verifica_login=verifica_email and verifica_senha
print(verifica_login)

#logica ou(or)


logica_ou= False or False or True
print(logica_ou)

      #Not
#  #Not
negacao= not True
print(negacao)

if not verifica_login:
    print("loga certo ai ...")
else:
    print("entra no programa")
