from time import sleep
def valida_num(n):
    if n.isdigit():
        return True
    return False

def valida_pergunta(op,pergunta):
    tam=len(pergunta)
    if pergunta.isalpha() and (tam==5 or tam==7):
        if pergunta in op:
            return True
        return False
    return False

def joken_po():
    resp=[]
    lista=['pedra','papel','tesoura','lagarto','spock']
    for i in range(2):
        pergunta = input('''Escolha uma opcao para se jogar: 

        [0] Pedra
        [1] Papel
        [2] Tesoura
        [3] lagarto
        [4] Spock
 
        Digite sua escolha jogador({:d}): '''.format(i+1)).lower()
        valida_pergunta(lista,pergunta)
        while not valida_pergunta(lista,pergunta):
            print('opçâo inválida...');
            sleep(1)
            pergunta = input('''Escolha  uma opcao para se jogar: 

            [0] Pedra
            [1] Papel
            [2] Tesoura
            [3] lagarto
            [4] Spock
 
            Digite sua escolha jogador({:d}): '''.format(i+1)).lower()
            pergunta=no_space(pergunta)
            valida_pergunta(lista,pergunta)
            
        resp.append(pergunta)
        
    print(resp)
    print('começando em..')
    sleep(1)
    print(1)
    sleep(1)
    print(2)
    sleep(1)
    print(3)
    sleep(3)
    #Sheldon seleciona Spock
    if resp[0]==lista[4]:
         if resp[1]==lista[4]:
             resultado="De novo!"
         elif resp[1]==lista[2] or res[1]==lista[0]:
             resultado='Bazinga'
         elif resp[1]==lista[3] or resp[1]==lista[1]:
             resultado='Raj trapaceou!'
    #Sheldon seleciona Pedra
    elif resp[0]==lista[0]:
         if resp[1]==lista[3] or resp[1]==lista[2]:
             resultado='Bazinga'
         elif resp[1]==lista[1] or resp[1]==lista[4]:
             resultado='Raj trapaceou!'
    #Sheldon seleciona papel
    elif resp[0]==lista[1]:
         if resp[1]==lista[0] or resp[1]==lista[4]:
             resultado='Bazinga'
         elif resp[1]==lista[2] or resp[1]==lista[3]:
             resultado='Raj trapaceou!'
    #Sheldon seleciona tesoura
    elif resp[0]==lista[2]:
          if resp[1]==lista[1] or resp[1]==lista[3]:
             resultado='Bazinga'
          elif resp[1]==lista[4] or resp[1]==lista[0]:
             resultado='Raj trapaceou!'
    #Sheldon seleciona lagarto
    elif resp[0]==lista[3]:
        if resp[1]==lista[4] or resp[1]==lista[1]:
            resultado='Bazinga'
        elif resp[1]==lista[0] or resp[1]==lista[2]:
            resultado='Raj trapaceou!'
            
            
             
    
    return resultado
        
        
n=input('digite o número de partidas: ')
while not valida_num(n):
    n=input('digite novamente número de partidas: ')
    valida_num(n)

k=0
while k<int(n):
  result=joken_po()
  print('caso#{0:d}: {1:1s}'.format(k+1,result))
  sleep(2)
  k+=1
