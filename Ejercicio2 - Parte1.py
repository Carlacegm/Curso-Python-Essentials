# -*- coding: utf-8 -*-
"""
@author: Carla Guerrero
"""

Datos_2021=(1,2,3,4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302)
cont=0
rep1=0
rep2=0
atp=0
pares=[0,0,0,0,0,0,0,0,0,0,0,0,0]
impares=[0,0,0,0,0,0,0,0,0,0]
atipicos=[0,0,0]

var1=len(Datos_2021)

for cont in range(var1):
    if (Datos_2021[cont]%2==0):
        pares[rep1]=Datos_2021[cont]
        rep1+=1
    else:
        impares[rep2]=Datos_2021[cont]
        rep2+=1
        
    if (Datos_2021[cont]>100):
        atipicos[atp]=Datos_2021[cont]
        atp+=1
    
    cont+=1
print(f"Números pares={pares}")
print(f"Números impares={impares}")
print(f"Valores atípicos={atipicos}")
