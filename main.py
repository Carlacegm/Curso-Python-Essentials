# -*- coding: utf-8 -*-
"""
@author: Carla Guerrero
"""    

var1=0
while var1!=2:
    opc=int(input("1. Consultar el tipo de valores predeterminados.\n2. Consultar el tipo de valores ingresados.\n3. Separar los datos de una tupla en pares, impares y atípicos.\n4. Ingresar una contraseña y validar.\n5. Encontrar los valores más altos y bajos dentro de los valores de un diccionario.\n6. Salir.\nEscoja una opción: "))
    
    try:
        if opc>0 and opc<7:
            x=opc/1
        else:
            x=opc/0
    
    except:
        print("Opción inválida.\nVuelva a ingresar una opción correcta.")
    
    else:
        if opc==1:
            import primermodulo as pm
            pm.primerejer()
            var1=0
        elif opc==2:
            import segundomodulo as sm
            sm.segundoejer()
            var1=0
        elif opc==3:
            import tercermodulo as tm
            tm.tercerejer()
            var1=0
        elif opc==4:
            import cuartomodulo as cm
            cm.cuartoejer()
            var1=0
        elif opc==5:
            import quintomodulo as qm
            qm.quintoejer()
            var1=0
        elif opc==6:
            var1=2