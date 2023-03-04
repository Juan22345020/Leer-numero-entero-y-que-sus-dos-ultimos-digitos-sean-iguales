# Determinar si los dos numeros ultimos son iguales


print("----------------------------------------------")
print("--------low dos ultimos digitos son iguales---")
print("----------------------------------------------")


# input

n = int(input("Digite el numero a revisar: "))

x = n //10
y = n%10


#procesing

if(x==y):
    print("Los ultimos dos digitos son iguales ")
else :
    print("Los ultimos digitos no son iguales ")