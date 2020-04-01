from time import *
def valida_num(n):
    if n.isdigit():
        return True
    return False
#retorna o respectico num na série de fib
def fib_recursivo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib_recursivo(n-1)+fib_recursivo(n-2)
#mostra a série para o usuário 
def fib_interativo(n):
    n1,n2=1,1
    if n==0:
        print(0)
    if n>=1:
        print(n1)
    if n==2:
       print(n2)
    if n>2:
        for i in range(2,n):
            prox=n1+n2
            print(prox)
            n1=n2
            n2=prox

#programa principal
n=input('digite o num de casos a serem analisados:')
while not valida_num(n):
    n=input('digite novamente o num de casos a serem analisados:')
    valida_num(n)
k=0
while k<int(n):
    num=int(input("digite um numero:"))
    while not valida_num(n):
        num=input('digite o num de casos a serem analisados:')
        valida_num(num)
    print("calculando a série de fib...")
    sleep(1)
    print("...")
    sleep(2)
    fib_interativo(int(num))
    print("Fib_recursivo({0:d}):{1:d}".format(int(num),fib_recursivo(int(num))))
    k+=1
    
