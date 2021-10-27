# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:57:40 2020

@author: andref
@author: joaoj
@author: nunoe
"""
from timeit import *
from jogos import *
from rastros import *
#from TheNiggerAI import*

#Recorrendo a nossa funcao, a nossa IA
#calcula a melhor forma de ganhar o jogo 
#de Rastros contra qualquer adversario
def win_Basilio(estado,jogador):
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
         

#Calcular melhor forma de S ganhar 
#Conforme as posicoes que a peca ocupa,
#sao atribuidos um dado numero de pontos,
#sendo privilegiado o rumo a sul e sudoeste (dando lhes maior "pontuacao")
#e "prejudicando" caso siga na direcao oposta
def  calcScoreWinS(estado,moves,win):
    # branco = estado.white
    # for black in blacks:
    #     if black[0] == 1:
    #            calc -= 4
    #     if black[1] == 1:
    #             calc+= 4    
    #     if black[0] == 2 :
    #         calc -= 3
    #     if black[1] == 2:
    #         calc += 3     
    #     if black[0]==3 : 
    #         calc-=2
    #     if black[1] ==3:
    #         calc+=2           
    #     if black[0] ==4: 
    #         calc -= 1
    #     if black[1] ==4:
    #         calc += 1    
    #     if black[0]==5: 
    #         calc+=1
    #     if black[1] ==5:
    #         calc-=1
    #     if black[0] ==6 :
    #         calc += 2
    #     if black[1] ==6:
    #         calc -= 2 
    #     if black[0] ==7 :
    #         calc += 3
    #     if black[1] ==7:
    #         calc -= 3
    #     if black[0] ==8 :
    #         calc += 4
    #     if black[1] ==8:
    #         calc -= 4
        # if black==(1,8) or black==(2,8) or black==(2,7):
        #     calc-25
    # calc=0
    # blacks=list(estado.blacks)
    # branco = estado.white
    # for black in blacks:
    #     if black[0] <=4 and black[1] >= 5:
    #         calc -= 2
    #     if black[0] >= 5 and black[1] <= 4:
    #         calc += 2       
    #     # if black[0] >=5 and black[1] >=5 :
    #     #     calc -=1
    #     # if black[0] <= 4 and black[1]  <=4:
    #     #     calc-=1       
    # return calc
#     calc=0
#     blacks=list(estado.blacks)
# # =============================================================================
# #     if (estado.white==(8,8) and ((8,7) and (7,8) and(7,7) in blacks)) or (estado.white==(1,1) and ((1,2) and (2,1) and (2,2)) in blacks) :
# #         calc-=100
# # =============================================================================
#     branco = estado.white
#     for black in blacks:
#         if black[0] <= 4:
#             calc -= 1
#         if black[1] >= 5:
#             calc-=1
            
#         if black[0] >= 5 :
#             calc += 1
#         if black[1] <= 4:
#             calc += 1
            
#         if black[0]<=3 : 
#            calc-=1
#         if black[1] >=6:
#            calc-=1
            
            
#         if black[0] >=6: 
#            calc+= 1
#         if black[1] <=3:
#            calc += 1
            
        
#         if black[0]<=2: 
#            calc-=1
#         if black[1] >=7:
#            calc-=1
        
#         if black[0] >=7 :
#            calc += 1
#         if black[1] <=2:
#            calc += 1                 
    #return calc        
    calc=0
    blacks=list(estado.blacks)
    white=estado.white         
    # if(white[0],white[1]-1) in moves and len(moves)==8:
    #     calc+= 10
    # elif(white[0]+1,white[1]-1) in moves and len(moves)==7 and (white[0],white[1]-1) not in moves:
    #     calc+=10
    # elif (white[0]+1,white[1]) in moves and (white[0],white[1]-1) not in moves and (white[0]+1,white[1]-1) not in moves :
    #     calc+=10
    # elif(white[0]+1,white[1]) in  moves and len(moves)==2 and ((white[0]+1,white[1]) in moves and white[0],white[1]+1 in moves):
    #     calc+=10
    
    # if len(moves)%2!=0:
    #     calc+=1  
    if (white[0]+1,white[1]-1) in moves:
        calc+=12  
    elif  (white[0]+1,white[1]) in moves:
        calc+= 8
    elif (white[0],white[1]-1) in moves:
        calc+=4
    # elif (white[0]-1,white[1]) in moves:
    #     calc+= 4
    elif (white[0]-1,white[1]-1) in moves or (white[0]+1,white[1]+1) in moves:
        calc+= 0   
    elif ((white[0]-1,white[1]) in moves) or ((white[0],white[1]+1) in moves):
        calc -= 8  
    elif (white[0]-1,white[1]+  1) in moves:
        calc-=12
    else:
        calc+= 1
    return calc
    
    
#Calcular a melhor forma de N ganhar 
#Conforme as posicoes que a peca ocupa,
#sao atribuidos um dado numero de pontos,
#sendo privilegiado o rumo a norte e nordeste (dando lhes maior "pontuacao")
#e "prejudicando" caso siga na direcao oposta
def  calcScoreWinN(estado,moves,win):
    calc=0
    blacks=list(estado.blacks)
    white=estado.white         
    # if(white[0],white[1]+1) in moves and len(moves)==7:
    #     calc+= 10
    # elif(white[0]-1,white[1]+1) in moves and len(moves)==6 and (white[0],white[1]+1) not in moves:
    #     calc+=10
    # elif (white[0]-1,white[1]) in moves and (white[0],white[1]+1) not in moves and (white[0]-1,white[1]+1) not in moves :
    #     calc+=10
    # elif(white[0]-1,white[1]) in  moves and len(moves)==2 and ((white[0]-1,white[1]) in moves and (white[0],white[1]-1) in moves):
    #     calc+=10
    # elif (white[0]-1,white[1]-1) in moves and  (white[0]+1,white[1]+1) in moves and (white[0],white[1]+1) not in moves and (white[0]-1,white[1]+1) not in moves and (white[0]-1,white[1]) not in moves :
    #     calc+=10
    # if len(moves)%2!=0:
    #     calc+=1
    if (white[0]-1,white[1]+1) in moves:
        calc+=12 
    elif  (white[0]-1,white[1]) in moves:
        calc+= 8   
    elif (white[0],white[1]+1) in moves:
        calc+=4
    # elif (white[0]-1,white[1]) in moves:
    #     calc+= 4 
    elif (white[0]+1,white[1]+1) in moves or (white[0]-1,white[1]-1) in moves:
        calc+= 0  
    elif ((white[0]+1,white[1]) in moves) or ((white[0],white[1]-1) in moves):
        calc -= 8   
    elif (white[0]+1,white[1]-1) in moves:
        calc-=12
    else:
        calc+= 1
    return calc
    
    # branco = estado.white
    # for black in blacks:
    #     if black[0] ==1:
    #            calc += 4
    #     if black[1] == 1:
    #             calc-= 4
            
    #     if black[0] == 2 :
    #         calc += 3
    #     if black[1] == 2:
    #         calc -= 3
            
    #     if black[0]== 3 : 
    #         calc+=2
    #     if black[1] ==3:
    #         calc-=2
            
            
    #     if black[0] ==4: 
    #         calc += 1
    #     if black[1] ==4:
    #         calc -= 1
            
        
    #     if black[0]==5: 
    #         calc-=1
    #     if black[1] ==5:
    #         calc+=1
        
    #     if black[0] ==6 :
    #         calc -= 2
    #     if black[1] ==6:
    #         calc += 2
        
    #     if black[0] ==7 :
    #         calc -= 3
    #     if black[1] ==7:
    #         calc += 3
        
    #     if black[0] ==8 :
    #         calc -= 4
    #     if black[1] ==8:
    #         calc += 4
            
        # if black==(7,1) or black==(8,2) or black==(7,2):
        #     calc-25
            
       
            
#     calc=0
#     blacks=list(estado.blacks)
    
# # =============================================================================
# #     if (estado.white==(8,8) and ((8,7) and (7,8) and(7,7) in blacks)) or (estado.white==(1,1) and ((1,2) and (2,1) and (2,2)) in blacks) :
# #         calc-=100
# # =============================================================================
#     branco = estado.white
#     for black in blacks:
#         if black[0] <=4:
#                calc += 1
#         if black[1] >= 5:
#                 calc+= 1
            
#         if black[0] >= 5 :
#             calc -= 1
#         if black[1] <= 4:
#             calc -= 1
            
#         if black[0]<=3 : 
#             calc+=1
#         if black[1] >=6:
#             calc+=1
            
            
#         if black[0] >=6: 
#             calc -= 1
#         if black[1] <=3:
#             calc -= 1
            
        
#         if black[0]<=2: 
#             calc+=1
#         if black[1] >=7:
#             calc+=1
        
#         if black[0] >=7 :
#             calc -= 1
#         if black[1] <=2:
#             calc -= 1
            
        # if black[0] ==1 :
        #     calc += 1
        # if black[1] ==8:
        #     calc += 1
        
        # if black[0] ==8 :
        #     calc -= 1
        # if black[1] ==1:
        #     calc -= 1
            
            
    # if estado.white==(7,7) and (((8,7) and (7,8)) in blacks):
        	#     for m in moves:
    #         if m[0]==estado.white[0]+1 and m[1]==estado.white[1]+1:
    #             calc+=1
    # if estado.white==(2,2) and (((1,2) and (2,1)) in blacks):
    #         for m in moves:
    #             if m[0]==estado.white[0]-1 and m[1]==estado.white[1]-1:
    #                 calc+=1
        
        
    # if (((1,2) and (2,1))) in blacks:
    #       for m in moves:
    #           if m==(2,2):
    #               calc-=1
    # elif (((8,7) and (7,8))) in blacks:
    #       for m in moves:
    #           if m==(7,7):
    #               calc-=1
          
    # 5
                        
# =============================================================================
#     if estado.white[0]<3 and estado.white[1]>6:
#         calc+=10-distancia(estado.white,(1,8))        
# =============================================================================
                
    
    #return calc
"""    
def constrain(tuple_white,blacks):
    dic={}
    if  (tuple_white[0]-1,tuple_white[1]) in blacks:
        dic["u"]=True
    if  (tuple_white[0]-1,tuple_white[1]+1)  in blacks:
        dic["ur"]=True
    if  (tuple_white[0],tuple_white[1]+1)   in blacks:
        dic["r"]=True
    if  (tuple_white[0]+1,tuple_white[1]+1)  in blacks:
        dic["dr"]=True
    if  (tuple_white[0]+1,tuple_white[1])  in blacks:
        dic["d"]=True
    if  (tuple_white[0]+1,tuple_white[1]-1) in blacks:
        dic["dl"]=True
    if  (tuple_white[0],tuple_white[1]-1)  in blacks:
        dic["l"]=True
    if  (tuple_white[0]-1,tuple_white[1]-1) in blacks:
        dic["ul"]=True
    if len(dic)>0:
        return dic
    return None
 """

#Calcular numero de movimentos que N pode efetuar numa dada posicao (estado)
def lenMovesN(estado,num):
    return num 

#Calcular numero de movimentos que S pode efetuar numa dada posicao (estado)         
def lenMovesS(estado,num):
    blacks=estado.blacks
    if (estado.white[0]+1,estado.white[1]) or (estado.white[0]+1,estado.white[1]-1) in estado.moves():
        num+=2
    return num

#Criacao do nosso jogador
ganhaBasilio = Jogador("ganhaBasilio",
                  lambda game, state:
                  alphabeta_cutoff_search_new(state,game,depth_for_all,eval_fn=win_Basilio))

#Jogo contra Basilio  
jogo1 = jogaRastros11(ganhaBasilio,basilio)
print(str(jogo1))
mostraJogo(jogo1[0])
#Passo a passo do jogo contra Basilio
mostraJogo(jogo1[0], verbose = True)
menos = 0


#Realizando o for que se apresenta abaixo, 
#obtemos, jogando como Sul, no minimo 85% de vitorias (quando
#corre menos bem) e no máximo 97%
for i in range(0,100):
    jogo1 = jogaRastros11(ganhaBasilio,basilio)
    #print(str(jogo1))
    #mostraJogo(jogo1[0])
    #mostraJogo(jogo1[0], verbose = True)
    if jogo1[1] == 1:
        menos += 1
print(menos)


#todosJog = [bacoco, obtusoSW, obtusoNE, arlivre, basilio,ganhaBasilio,nigger]
#campeonato = jogaRastrosNN(todosJog, todosJog, nsec=10)
#faz_campeonato(todosJog)




        
        

    
        
        
        
        
        