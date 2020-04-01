from time import *
def valida_num(n):
    if n.isdigit():
        return True
    return False
#função que testa se a entrada da dimensão
def valida(n):
    if n>=0 and n<=60:
         return True
    return False

def le_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end="")
        print("\n")
#função que retorna uma matriz quadrada diagonal
def cria_matri():
    try:
        N=int(input("digite o num de dimensão da sua matriz quadrada: "))
        while not valida(N):
            N=int(input("digite o num de dimensão da sua matriz quadrada: "))
            valida(N)
        print("criando a matriz...")
        print('1')
        sleep(1)
        print('2')
        sleep(1)
        print('3...')
        sleep(3)
        
        print("Matrix({:d}x{:d})".format(N,N))
        
        M=[0]*N
        for i in range(N):
            M[i]=[0]*N
        for j in range(N):
            M[j][j]=1
        le_matriz(M)
    except(ValueError):
        print("valor inválido")
#programa principal
n=input('digite o num de casos a serem analisados:')
while not valida_num(n):
    n=input('digite novamente o num de casos a serem analisados:')
    valida_num(n)
k=0
while k<int(n):
  cria_matri()
  k+1

