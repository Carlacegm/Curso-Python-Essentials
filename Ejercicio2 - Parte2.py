# -*- coding: utf-8 -*-
"""
@author: Carla Guerrero
"""

contr=input("Ingrese su contraseña: \nDebe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.\nDebe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.\nDebe contener al menos un número entre 0 y 9.\nDebe contener un símbolo especial entre: $,%,*,@\nTamaño mínimo de 5 caracteres y máximo de 15.\n")
var1=len(contr)
cont=0
clst1=0
clst2=0
clst3=0
clst4=0
lst1=["a","b","c","d","e","f","g","h","i","j"]
lst2=["K","L","M","N","O","P","Q","R","S","T"]
lst3=["0","1","2","3","4","5","6","7","8","9"]
lst4=["$","%","*","@"]

if var1>=5 and var1<16:
    for cont in range(var1):
        if contr[cont] in lst1:
            cont+=1
            clst1+=1
        elif contr[cont] in lst2:
            cont+=1
            clst2+=1
        elif contr[cont] in lst3:
            cont+=1
            clst3+=1
        elif contr[cont] in lst4:
            cont+=1
            clst4+=1
        else:
            print("Constraseña inválida.")
            break
   
    if clst1!=0 and clst2!=0 and clst3!=0 and clst4!=0:
        print("Contraseña válida.")
    else:
        print("Constraseña inválida.")
            
else:
    print("Contraseña inválida.\nSu contraseña debe tener un tamaño mínimo de 5 caracteres y máximo de 15")
