#funções de validaçao
def valida_frase(f):
    tam=len(f)
    if f.isalpha() and tam>0 and  tam<=100:
        return True
    return False
def valida_char(char):
    if char.isalpha() and len(char)==1:
        return True
    return False
def valida_num(n):
    if n.isdigit():
        return True
    return False

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        #chamda recursiva
        mergeSort(left)
        mergeSort(right)
        
        i = 0
        j = 0
        #contador da lista principal
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
def count_letrasporseg(myStr):
    resp=[]
    char=myStr[0]
    count=1
    k=1
    while k<(len(myStr)):
        if char==myStr[k] :
            count+=1
        else:
            if myStr[k]==-1:
                resp.append(chr(char)+'('+str(count)+')')
            else:
                resp.append(chr(char)+'('+str(count)+')')
                count=1
                char=myStr[k]

        k+=1
    return resp
           
def busca(char,v):
    for i in range(0,len(v)):
        if v[i][0]==char:
            return i
    return -1
def count_letters():
    #num de strins a serem avaliadas 
    num=input("digite o número de casos a serem analisados:")
    while not valida_num(num):
        num=input("digite novamente um número de casos a serem analisados:")
        valida_num(num)
    k=0
    resp=''
    while (k<int(num)):
        frase=input("digite uma frase a ser analisada: ").lower()
        while not valida_frase(frase):
            frase=input("digite novamente uma frase a ser analisada: ")
            valida_frase(frase)
        char=input("digite uma letra para ser analisada: ").lower()
        if not valida_char(char):
            resp='consulta inválida'
        #para ordenar a frase é necessário de um vetor numérico
        letras_ASC=[]
        for i in range(len(frase)):
            letras_ASC.append(ord(frase[i]))
        #ordenando a frase
        mergeSort(letras_ASC)
        letras_ASC.append(-1)
        print(letras_ASC)
        if len(frase)>1:
            myResp=count_letrasporseg(letras_ASC)
        print(myResp)
        if  resp!='consulta inválida':
            if ord(char) in letras_ASC:

                print(myResp[busca(char, myResp)][2])
        else:
            if resp=='consulta inválida':
                print('consulta inválida')
            else:
                print("operaçao nao realizada")
            
        k+=1
#programa principal        
count_letters()
            
    
    
