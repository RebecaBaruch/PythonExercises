print("Digite um número inteiro: ")
num1 = int(input())

print("Digite outro número inteiro: ")
num2 = int(input())

print("Digite um número real: ")
numReal = float(input())

prod = (2*num1)*(num2/2)
sum = (3*num1) + numReal
cubo = numReal**3

print("(2X",num1,")X(",num2,"/2) = ",prod);
print("(3X",num1,")+",numReal," = ",sum)
print(numReal,"^3 = ",cubo)