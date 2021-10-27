# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:40:02 2020

@author: nunoe
"""
from searchPlus import* 
from copy import copy,deepcopy

class PuzzleColares:
    pulseiras={ "1":["g","g","g","g","g","b","g","g","p","p","r","r","r","r","r","r","r","r","r","g"],
           "2":["b","b","b","b","b","b","b","p","p","p","p","p","p","g","g","p","p","g","g","b"]}
    obj={ "1":["g","g","g","g","g","g","g","p","r","r","r","r","r","r","r","r","r","g","g","g"],
           "2":["b","b","b","b","b","b","b","p","p","p","p","p","p","p","p","p","p","g","b","b"]}
    
    
    def __init__(self,initial=pulseiras,goal=obj):
        self.initial,self.goal=initial,goal
        self.verificaInicial()
        
    
    def verificaInicial(self):
        var=[]
        y=0
        differentColors=[]
        contador=[]
        conta9s=0
        conta10s=0
        for x in self.initial:
            var.append(self.initial[str(y+1)])                
            y+=1
        for x in range(len(var)-1) :
            if var[x][3]!=var[x+1][17] or var[x][7]!=var[x+1][13] or len(var[x])!=20:
                return False
        for x in var :
            for y in range(len(x)):
                if not differentColors.__contains__(x[y]):
                    if (y==7 or y==3) and var.index(x)!=(len(var)-1):
                        pass
                    else:
                        differentColors.append(x[y])  
                        contador.insert(differentColors.index(x[y]),1)
                elif (y==7 or y==3) and var.index(x)!=len(var)-1:
                    pass
                else:
                    contador[differentColors.index(x[y])]+=1
                    
        for x in contador:
            if int(x)==10:
                conta10s+=1
            if int(x)==9:
                conta9s+=1
        return conta9s==len(contador)-2 and conta10s==2
                
            
    def actions(self,estado):
        teste=estado.keys()
        accoes=[]
        for x in teste:
            accoes.append(x+"H")
            accoes.append(x+"aH")
        return accoes
    
    
    
    def result(self, estado,accao):
        resultado=deepcopy(estado)
        
            
            
        accoes=self.actions(estado)
        if accao in accoes:
            sentido=accao.replace(accao[0], "") #guarda o sentido H ou aH
            anel=accao[0] #guarda o num anel que vai rodar
            anelAnt=str(int(anel)-1)
            anelSeg=str(int(anel)+1)
            if sentido=="H":
                for x in range(len(resultado[anel])):
                    if x==0:
                        atual=resultado[anel][x]
                    if x< len(resultado[anel])-1:
                        proximo=resultado[anel][x+1]
                        resultado[anel][x+1]=atual
                        atual=proximo
                    else:
                        resultado[anel][0]=atual        
            
            else:
                for x in range(len(resultado[anel])):
        
                    if x!= len(resultado[anel])-1:  
                        resultado[anel][x]=resultado[anel][x+1]
                    else:
                        resultado[anel][x]=estado[anel][0]   
           
                if list(resultado).index(anel)==0:
                    resultado[anelSeg][13]=resultado[anel][7] 
                    resultado[anelSeg][17]=resultado[anel][3]
                
                elif list(resultado).index(anel)==len(resultado)-1:
                    resultado[anelAnt][3]=resultado[anel][17] 
                    resultado[anelAnt][7]=resultado[anel][13]
                
                else:
                    resultado[anelAnt][3]=resultado[anel][17] 
                    resultado[anelAnt][7]=resultado[anel][13]
                    resultado[anelSeg][13]=resultado[anel][7] 
                    resultado[anelSeg][17]=resultado[anel][3]
                
            
        return resultado   

    
    def goal_test(self,estado):
        
        for anel in range(len(estado)):
            for element in range(len(estado[str(anel+1)])):
                if estado[str(anel+1)][element]!=self.goal[str(anel+1)][element]:  
                    return False
        return True
    
    
    
    
    def path_cost(self, cost,state,action,new_state):
        
        
        return cost+1
    
    def display(self,estado):
        row=9
        matriz = [["" for i in range(9+6*(len(self.initial)-1))] for j in range(9)]
        #contadores de cima para baixo de cada circulo
        
        col=9+6*(len(self.initial)-1)
        
        
        for i in range(0,row):
            for j in range(0,col):
                if i==0 or i==8:
                    if j%3==0 and j%6!=0  and j>0 and j<len(matriz[0]):
                        anel=int(j/6)+1
                        if i==0:
                            matriz[i][j]=estado[str(anel)][19]
                            matriz[i][j+1]=estado[str(anel)][0]
                            matriz[i][j+2]=estado[str(anel)][1]
                        else:
                            matriz[i][j]=estado[str(anel)][11]
                            matriz[i][j+1]=estado[str(anel)][10]
                            matriz[i][j+2]=estado[str(anel)][9]
                        
                elif i== 1 or i==7:
                    if (j==2 or j<len(matriz[0])-1 ) and ((j!=0 and (j-2)%6==0)) :
                        anel=int(j/6)+1
                        if i==1:
                            matriz[i][j]=estado[str(anel)][18]
                        else:
                            matriz[i][j]=estado[str(anel)][12]
          
                    elif (j!=0 and j%6==0):
                        anel=int(j/8)+1
                        if i==1:
                            matriz[i][j]=estado[str(anel)][2]
                        else:
                            matriz[i][j]=estado[str(anel)][8]

                        
                elif i==3:
                    if (((j==0 or j%6==0) and j<len(matriz[0])-3)):
                        anel=int(j/6)+1
                        matriz[i][j]=estado[str(anel)][16]
                        matriz[i+1][j]=estado[str(anel)][15]
                        matriz[i+2][j]=estado[str(anel)][14]
                        
                    elif (j==8 or  (j>8 and (j-2)%6==0)):
                        if j==8:
                            anel="1"
                        else:
                            anel=int(j/6)
                        matriz[i][j]=estado[str(anel)][4]
                        matriz[i+1][j]=estado[str(anel)][5]
                        matriz[i+2][j]=estado[str(anel)][6]
                        
                        
                        
                        
                elif i==2 :
                    if (j-1)%6 ==0:
                        if j<len(matriz[0])-2:
                            anel=int((j-1)/6)+1
                            matriz[i][j]=estado[str(anel)][17]

                        else:
                            anel=int((j-1)/6)
                            matriz[i][j]=estado[str(anel)][3]
                elif i==6:
                    if (j-1)%6 ==0:
                        if j<len(matriz[0])-2:
                            anel=int((j-1)/6)+1
                            matriz[i][j]=estado[str(anel)][13]
                        else:
                            anel=int((j-1)/6)
                            matriz[i][j]=estado[str(anel)][7]
                   
 
        
                
        
        print('\n'.join(["".join(['{:2}'.format(item) for item in row]) 
        for row in matriz]))        

                        
    
                                
            
        
        
        
    def exec(p,estado,accoes):
        """ Executa uma sequência de acções a partir do estado
        devolve um par (estado, custo) depois de imprimir
        """
        custo = 0
        for a in accoes:
            seg = p.result(estado,a)
            custo = p.path_cost(custo,estado,a,seg)
            estado = seg
        return (estado,custo)                
                
                
                
                
                
                
     

            
        
            
pulseiras={ "1":["g","g","g","g","g","b","g","g","p","p","r","r","r","r","r","r","r","r","r","g"],
            "2":["b","b","b","b","b","b","b","p","p","p","p","p","p","g","g","p","p","g","g","b"]}
     
          
        
p=PuzzleColares({ "1":["g","g","g","g","g","b","g","g","p","p","r","r","r","r","r","r","r","r","r","g"],
            "2":["b","b","b","g","b","b","b","p","p","p","p","p","p","g","g","p","p","g","g","b"],"3":["b","b","b","g","b","b","b","p","p","p","p","p","p","g","g","p","p","g","g","b"]})
p.result(p.initial, "1aH")
a=p.exec(p.initial, p.actions(p.initial))
p.display(list(a)[0])
  


