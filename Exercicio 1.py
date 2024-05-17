#solicitar ao usuário que digite
numero =float(input("digite um numero: "))
#Verificar se o número é negativo, positivo ou zero
if numero > 0:
    print("o numero é positivo:")
elif numero < 0:
    print("o numero é negativo:")
else:
    print("o numero é zero")
