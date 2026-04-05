# technical test 2

#yes, the function is working and it is correct
def somar(a, b=10): #'b' assumes the value 10 if it is not informed
    return a + b  #return a + b

print(somar(5)) #15 (b uses the default value 10)

print(somar(5, 3))  #8 (a=5, b=3)

print(somar(b=2, a=4))  #6 (a=4, b=2)