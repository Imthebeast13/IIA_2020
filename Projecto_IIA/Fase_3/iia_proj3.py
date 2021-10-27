# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:12:40 2020

@author: nunoe
"""
from copy import copy,deepcopy
from rastros import*
from utils import *
from jogos import*
from search import* 
from geneticSolo import *
import random
import string
import math    
import time



def win_Basilio(jogador,estado):
    movimentos=estado.moves()
    if estado.terminou == 1:
        return 100 if jogador == "S" else -100
    elif estado.terminou == -1:
        return 100 if jogador == "N" else -100
    else: 
        if jogador=="N":
            return calcScoreWinN(estado,movimentos,(1,8)) #formaPretasN(estado)
        else:
            return calcScoreWinS(estado, movimentos, (8,1))
        
def  calcScoreWinS(estado,moves,win):
   
    calc=0
    blacks=list(estado.blacks)
    white=estado.white         
    
    calc-=distancia(white,(8,1))
            
    if (white[0]+1,white[1]-1) in moves:
        calc+=10
        
    elif  (white[0]+1,white[1]) in moves:
        calc+= 7
    
    elif (white[0],white[1]-1) in moves:
        calc+=3
        
    elif (white[0]-1,white[1]-1) in moves or (white[0]+1,white[1]+1) in moves:
        calc+= 0
        
    elif ((white[0]-1,white[1]) in moves) or ((white[0],white[1]+1) in moves):
        calc -= 3
        
    elif (white[0]-1,white[1]+  1) in moves:
        calc-=10
    
    else:
        calc+= 1
    return calc
    
    

def  calcScoreWinN(estado,moves,win):
    
    calc=0
    blacks=list(estado.blacks)
    white=estado.white         
    
    calc-=distancia(white,(1,8))
 
    if (white[0]-1,white[1]+1) in moves:
        calc+=10
        
    elif  (white[0]-1,white[1]) in moves:
        calc+= 7
        
    elif (white[0],white[1]+1) in moves:
        calc+=3
        
    elif (white[0]+1,white[1]+1) in moves or (white[0]-1,white[1]-1) in moves:
        calc+= 0
        
    elif ((white[0]+1,white[1]) in moves) or ((white[0],white[1]-1) in moves):
        calc -= 3
        
    elif (white[0]+1,white[1]-1) in moves:
        calc-=10
    
    else:
        calc+= 1
    return calc

def dist_Obj(jogador,estado):
    if jogador=="S":
        obj=(8,1)
    else:
        obj=(1,8)
    return distancia(estado.white,obj)

def dist_Base(jogador,estado):
     if jogador=="S":
        obj=(1,8)
     else:
        obj=(8,1)
     return distancia(estado.white,obj)
         
                     
            
class Jogador():
    def __init__(self, nome, pesos,funcs):
        self.nome = nome
        self.pesos =pesos
        self.funcs=funcs
        self.depth=1
        self.fun=lambda game,state:alphabeta_cutoff_search_new(state,game,self.depth,eval_fn=self.aval_pesos)
    def display(self):
        print(nome+" ")
    def aval_pesos(self,estado,jogador):
        total=0
        for i in range(len(self.funcs)):
            total+=self.funcs[i](jogador,estado)*self.pesos[i]
        return total
   
def torneioDeK(ordered_dicionario,players,k,escolhidos_elitismo):
    listmaxs=[]
    for i in range(2):
        k_selected_prov=deepcopy(players)
        for x in listmaxs:
            for y in k_selected_prov:
                if y.nome==x.nome:  
                    k_selected_prov.remove(y)
        k_selected_players=[]
        for x in range(k):
            rand=random.choice(k_selected_prov)
            k_selected_prov.remove(rand)
            k_selected_players.append(rand)
        del k_selected_prov
        currMax=-1
        curr_second_max=-1
        curr_best_player=k_selected_players[0]
        for x in k_selected_players:
            if ordered_dicionario[x.nome]>currMax:
                curr_best_player=x
                currMax=ordered_dicionario[x.nome]
        listmaxs.append(curr_best_player)
    print("escolhidos para K:")
    i=0
    for x in listmaxs:
        print(str(i)+": " + str(x.pesos) )
        i+=1
    return listmaxs        
 
def recombine_new(array,x, y):
    n = len(x)
    c = random.randrange(0, n)
    array.append(x[:c] + y[c:])
    array.append(y[:c]+x[c:])

    

def elitism(elit,players,ordered_dicionario):
    elitismo= elit*len(players)
    if (math.floor(elitismo))%2==0:
        elitismo=(math.floor(elitismo))
    else:
        elitismo=(math.ceil(elitismo))
    temp=elitismo
    next_gen=[]
    for x in reversed(ordered_dicionario):
        if temp!=0:
              for y in players:
                  if y.nome==x:
                      next_gen.append(y)
                      temp-=1
                      break
        else:
            del temp
            break
    return next_gen




def mutate(x, gene_pool, pmut):
    for weight in range(len(x)):
        if random.uniform(0, 1) >= pmut:
            continue
        else:
            print("O peso: " +str(x[weight]) + " mutou")
            x[weight]=random.choice(gene_pool)

    return x
    
        
def coevol(gen,dim,gene_pool=range(-20,20),elit=0.2,p_mut=0.1,k_rivais=2,lim_profs=[4,5],jogo= Rastros,caracts = [dist_Base,dist_Obj,win_Basilio],numJogos=6
):
    k_rivais=int(dim/3)
    population=init_population(dim,gene_pool,len(caracts))
    players=[]
    letrasm=string.ascii_lowercase
    letrasM=string.ascii_uppercase
    letras_tot=letrasM+letrasm
    for guy in population:
        novoPlayer = Jogador(''.join(random.choice(letras_tot) for i in range(10)),guy,caracts)
        players.append(novoPlayer)
    
    for x in players:
        print("jogador " + x.nome + "  pesos: " + str(x.pesos) + "\n")
        
      
    i=0
    elitMax=[]
    while i<gen-1:
    
        dicionario={}
        for x in players:
            dicionario[x.nome]=1
        fitness_taca(players,jogo,dicionario,numJogos)
    #print(dicionario)
        ordered_dicionario = {}
        sorted_keys = sorted(dicionario, key=dicionario.get)  # [1, 3, 2]

        for w in sorted_keys:
            ordered_dicionario[w] = dicionario[w]
            
        escolhidos_elitismo=elitism(elit,players,ordered_dicionario)
        print("elitismo: ")
        b=1
        for x in escolhidos_elitismo:
           print(str(b)+": " + str(x.pesos))
           b+=1
    
        parents=torneioDeK(ordered_dicionario,players,k_rivais,escolhidos_elitismo)
        guys=[]
        for parent in parents:
            guys.append(parent.pesos)
        for x in guys:
            print("futuro pai/mae " + str(x))
        print("\n")
        prov_population=[]
        array=[]
        while (len(prov_population)+len(escolhidos_elitismo)) != dim:
            recombine_new(prov_population,guys[0],guys[1])
        for x in prov_population:
            mutate(x,gene_pool,p_mut)
    
        for x in escolhidos_elitismo:
            prov_population.append(x.pesos)
    #print(len(prov_population))
    #print(juntas)
    #print(escolhidos_elitismo)
        del players
        players=[]
        for guy in prov_population:
            novoPlayer = Jogador(''.join(random.choice(letrasm+letrasm) for i in range(10)),guy,caracts)
            players.append(novoPlayer)            
        i+=1
    # elitMax=random.choice(escolhidos_elitismo).pesos
    # print(elitMax)
    # return elitMax
    
    elitMax=[]
    dicionario={}
    for x in players:
        dicionario[x.nome]=1
    fitness_taca(players,jogo,dicionario,numJogos)
    #print(dicionario)
    ordered_dicionario = {}
    sorted_keys = sorted(dicionario, key=dicionario.get)  # [1, 3, 2]

    for w in sorted_keys:
        ordered_dicionario[w] = dicionario[w]
    escolhidos_elitismo=elitism(elit,players,ordered_dicionario)
    
       
    elitMax=escolhidos_elitismo[0].pesos
    print("Eis os pesos obtidos: " +str(elitMax))
    return elitMax

def jogar(jog1, jog2,jogo):
    ### jog1 e jog2 são jogadores com funções que dado um estado do jogo devolvem a jogada que escolheram
    ### devolve uma lista de jogadas e o resultado 1 se S ganha
    game =jogo() 
    estado=game.initial
    proxjog = jog1
    lista_jogadas=[]
    while not game.terminal_test(estado):
        jogada = proxjog.fun(game, estado)
        estado=game.result(estado,jogada)
        lista_jogadas.append((proxjog.nome, jogada))
        proxjog = jog2 if proxjog == jog1 else jog1
    return  estado.terminou


def fitness_taca(jogadores,game,dicionario,numJogos):
    localDic={}
    for x in jogadores:
        localDic[x.nome]=0
    lista_nao_verificaveis=[]
    lista_jogos=[]
    lista_jogadores_nao_emparelhados=deepcopy(jogadores)
    count=0
    while len(lista_jogadores_nao_emparelhados)!=0:
        jog=random.choice(lista_jogadores_nao_emparelhados)
        lista_jogadores_nao_emparelhados.remove(jog)
        adv=random.choice(lista_jogadores_nao_emparelhados)
        lista_jogadores_nao_emparelhados.remove(adv)
        
        
        jog.depth=1
        jog.fun=lambda game,state:alphabeta_cutoff_search_new(state,game,jog.depth,eval_fn=jog.aval_pesos)
        adv.depth=1
        adv.fun=lambda game,state:alphabeta_cutoff_search_new(state,game,adv.depth,eval_fn=adv.aval_pesos)
        for x in range(0,int(numJogos/2)):
            lista_jogos.append((jog.nome, adv.nome,jogar(jog,adv, game)))
            lista_jogos.append((adv.nome,jog.nome,jogar(adv,jog, game)))
         
        jog.depth=2
        jog.fun=lambda game,state:alphabeta_cutoff_search_new(state,game,jog.depth,eval_fn=jog.aval_pesos)
        adv.depth=2
        adv.fun=lambda game,state:alphabeta_cutoff_search_new(state,game,jog.depth,eval_fn=adv.aval_pesos)
        
        for x in range(0,numJogos-int(numJogos/2)):
            lista_jogos.append((jog.nome, adv.nome,jogar(jog,adv, game)))
            lista_jogos.append((adv.nome,jog.nome,jogar(adv,jog, game)))

        
    for x in lista_jogos:
        if x[2]==1:
            localDic[x[0]]+=1
        else:
            localDic[x[1]]+=1
    for x in localDic:
        for y in jogadores:
            if x == y.nome:
                print("peso " + str(y.pesos) + "   wins: " + str(localDic[x])  )
                break
    novaLista=[]
    for x in localDic:
        # print(str(localDic[x])+"\n\n\n")
        if math.floor((localDic[x]))>math.floor((numJogos)):     
            for jogador in jogadores:
                if jogador.nome==x:
                    novaLista.append(jogador)
                    break
        if math.floor((localDic[x]))==math.floor(numJogos) and x not in lista_nao_verificaveis:
            nome=""
            for jogo in lista_jogos:
                if jogo[0] == x or jogo[1]==x:
                    nome=random.choice([jogo[0],jogo[1]])
                    lista_nao_verificaveis.append(jogo[1])
                    lista_nao_verificaveis.append(jogo[0])
                    break
            for jogador in jogadores:
                if jogador.nome==nome:
                    novaLista.append(jogador)
                    break
   
    for x in novaLista:
        dicionario[x.nome]+=1
    if len(novaLista)!=1:
       print("\n")
       return fitness_taca(novaLista, game, dicionario,numJogos)
    return dicionario
p=coevol(5,32)



    
#     ### faz todos os jogos com timeout de nsec por jogada
#     campeonato = jogaRastrosNN(listaJogadores, listaJogadores, nsec)
#     ### ignora as jogadas e contabiliza quem ganhou
#     resultado_jogos = [(a,b,n) for (a,b,(x,n)) in campeonato]
#     tabela = dict([(jog.nome, 0) for jog in listaJogadores])
#     for jogo in resultado_jogos:
#         if jogo[2] == 1:
#             tabela[jogo[0]] += 1
#         else:
#             tabela[jogo[1]] += 1
#     classificacao = list(tabela.items())
#     classificacao.sort(key=lambda p: -p[1])
#     print("JOGADOR", "VITÓRIAS")
#     for jog in classificacao:
#         print('{:11}'.format(jog[0]), '{:>4}'.format(jog[1]))
































