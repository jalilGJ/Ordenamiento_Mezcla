# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:16:52 2021

@author: jalil
"""
import random # se importa la libreria para poder generar numeros aleatorios 

def merge_sort(data):
    mid = len (data) //2 # divide la mitad del arreglo
    if len(data)> 1: #si la longitud del data es mayor a uno 
        L=data[mid:] # darreglo obteniendo los valores que se encuentran en la izquierda
        R=data[:mid] # los valores que se encuentran en la derecha del arreglo
        
        data.clear()#refreash
        # se hace dos llamadas recursivas 
        merge_sort(L) # arreglo de la izquierda
        merge_sort(R) # arreglo de la derecha esto va ser que se dividadan 
        #hasta que todos los elemntos sean igual que uno
        
        #Metodo  para hacer el ordenamineto por mezcla
        while len(L)>0 and len(R)>0:# longitud del arreglo de la izquierda sea mayor a cero y la longitud 
            #del arreglo de la derecha sea mayor a cero
            if L[0]< R[0]: #si el elemento  que se encuentra en la posicion cero del arreglo de la izquierda 
                #es menor al elemento que se encuentra en la posicion cero del arreglo de la derecha
                data.append(L.pop(0)) # agrega al arreglo data el elemento que esta en la posicion cero 
            else:# si no
                data.append(R.pop(0)) # agrega el elemento de la posicion cero del arreglo
              
                
        while len(L) >  0: # cuando la longitud del lado izquierda sea mayor a cero va a agregar el arreglo data el elemento que se encuentre la posicion cero 
            data.append(L.pop(0))#agrega
           
        while len (R) > 0: #  pasa con el arreglo de la derecha
            data.append(R.pop(0))
        
    return data # retorna la lista ordenada
       
print (" \n ALGORITMO DE ORDENAMIENTO EXTERNO MEZCLA\n")
data =[random.randint(-50, 50) for i in range(20)] #se genera un arreglo, un dato a la cual estoy generando.

print(f"arreglo original:{data} \n") # se imprime el arreglo original para que se pueda notar cuales son los elementos que se ordenaron
x=merge_sort(data)
print(f"Arreglo ordenado:{x} \n") # imprimir el arreglo ordenado 
