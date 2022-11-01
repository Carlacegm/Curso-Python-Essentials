# -*- coding: utf-8 -*-
"""
@author: Carla Guerrero
"""
def quintoejer():
    def valores(ing,alt,baj):
        cont1=0
        cont2=0
        pos1=-1
        pos2=0
        lst1=[0]*alt
        lst2=[0]*baj
        
        if ing==1:
            dic1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
            var1=list(dic1.values())
            var1.sort()
            for cont1 in range(alt):
                lst1[cont1]=var1[pos1]
                cont1+=1
                pos1-=1
            for cont2 in range(baj):
                lst2[cont2]=var1[pos2]
                cont2+=1
                pos2+=1
                
            tpl=tuple(lst2)
            print(f"Los {alt} valores altos son: {lst1}")
            print(f"Los {baj} valores bajos son: {tpl}")
        
        elif ing==2:
            dic2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tplC":(87,12,56,987,-61)}
            lst=list(dic2["tplA"]+dic2["tplB"]+dic2["tplC"])
            lst.sort()
            for cont1 in range(alt):
                lst1[cont1]=lst[pos1]
                cont1+=1
                pos1-=1
            for cont2 in range(baj):
                lst2[cont2]=lst[pos2]
                cont2+=1
                pos2+=1
                
            tpl=tuple(lst2)
            print(f"Los {alt} valores altos son: {lst1}")
            print(f"Los {baj} valores bajos son: {tpl}")
       
        elif ing==3:
            dic3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
            var1=list(dic3.values())
            var1.sort()
            for cont1 in range(alt):
                lst1[cont1]=var1[pos1]
                cont1+=1
                pos1-=1
            for cont2 in range(baj):
                lst2[cont2]=var1[pos2]
                cont2+=1
                pos2+=1
        
        elif ing==4:
            dic4={"lstA":[4,6,-12,56,-9,5.7,33,100],"lstB":[9,0,81,-2,-56,],"lstC":[12,31,87,1,0,4,-11]}
            lst=dic4["lstA"]+dic4["lstB"]+dic4["lstC"]
            lst.sort()
            for cont1 in range(alt):
                lst1[cont1]=lst[pos1]
                cont1+=1
                pos1-=1
            for cont2 in range(baj):
                lst2[cont2]=lst[pos2]
                cont2+=1
                pos2+=1
                
            tpl=tuple(lst2)
            print(f"Los {alt} valores altos son: {lst1}")
            print(f"Los {baj} valores bajos son: {tpl}")
            
        return 
    
    
    var1=0
    while var1!=2:
        opc=int(input("1. Demostración del cálculo de valores altos y bajos en diccionarios.\n2. Salir.\nEscoja una opción: "))
        if opc==1:
            cont=0
            while cont==0:
                ing=int(input("1. {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}\n2. {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}\n3. {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}\n4. {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}\nEscoja un diccionario: "))
                if ing==1 or ing==2 or ing==3 or ing==4:
                    alt=int(input("Ingrese el número de valores altos que desea mostrar: "))
                    baj=int(input("Ingrese el número de valores bajos que desea mostrar: "))
                    valores(ing, alt, baj)
                    cont+=1
                else:
                    print("Opción inválida.")
                    cont=0
            var1=0
        elif opc==2:
            var1=2
        else:
            print("Opción inválida.")
            var1=0
    
    return
        

