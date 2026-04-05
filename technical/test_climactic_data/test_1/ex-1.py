#technical test 1

numeros = [1, 2, 3, 4, 5, 6]  #creates a list of numbers

resultado = []  #stores the values

for n in numeros: #loop that goes through each number in the list
    if n % 2 == 0:  #checks if it is even
        resultado.append(n * 2)  #if it's even, multiply by 2 and store
print(resultado)  #returns the result
 
#returned value [4, 8, 12]