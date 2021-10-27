from utilsAA import *
import numpy as np
import sklearn
import matplotlib.pyplot as plt

def medias(ind):
    soma = 0
    for i in range(0, len(plane_data[0])):
        soma+=plane_data[0][i][ind]
    return soma/(len(plane_data[0]))

plane_data=load_data('airline.csv')



print(medias(15))
mediaC = medias(15)
contador = 0
for j in range(0, len(plane_data[0])):
    if(plane_data[0][j][15] > mediaC):
        print(plane_data[0][j][0])
        contador+=1

print(contador)
print(plane_data[0])

