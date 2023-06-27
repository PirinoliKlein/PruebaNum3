listacuarto = [[1,2,3,4,5],[6,7,8,9,10]]
listarut=[]
listamascota=[]
fila=[]
columna=[]
contador = 0
acum = 0


#Validar opc
def validad_opc():
    while True:
        try:
            opc = int(input("Ingrese su opcion: "))
            if opc in(1,2,3,4):
                return opc
            else:
                ("ERROR! opcion no valida!")
        except:
            ("ERROR! debe ingresar un numero entero!")    

#Validar un rut 
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
               
                return rut
                
            else:
                print("ERROR! rut no valido!")
        except:
            print("ERORR! el rut no debe tener puntos ni digito verificador!")            

#Validar nombre
def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! nombre ingresado no valido!")  

#Validar un correo
def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("etc")
                  
#Validar cantidad de algo
def validar_cantidad():
    while True:
        try:
            cantidad_dias = int(input("Ingrese cantidad de dias: "))
            if cantidad_dias >= 1 and cantidad_dias <= 250:
                return cantidad_dias
            else:
                print("ERROR! dias excedidos!")
        except:
            print("ERROR! debe ingresar numero enteros!")                  

def validar_mascota_nom():
    while True:
        nombre_mas = input("Ingrese nombre de su mascota: ")
        if len(nombre_mas.strip()) >=3 and nombre_mas.isalpha():
            return nombre_mas
        else:
            print("ERROR! nombre ingresado no valido!")  

def habitaciones_mascota():
    numero=1
    
    print("""
    Fila X
    Columna Y""")
    
    

    

            

def validar_habitacion():
    while True:
        try:
            fila = int(input("Ingrese fila donde esta su mascota: "))
            columna = int(input("Ingrese columna donde estara su mascota: "))
            if fila >=1 and fila <=10: 
                return fila 
            if columna == 1 and columna == 2:
                return columna
            else:
                print("ERROR! Fila incorrecta")
        except:
            print("ERROR! columna incorrecta!")
                
def buscar_rut():               
    rut = validar_rut()
    print(listarut)
    if rut in listarut:
        listarut = listarut.insert(rut)
        print(listacuarto)(listarut)


def total_pagar():
    rut = validar_rut
    if rut in listarut:
        pagar = validar_cantidad *1500
        print("Su total a pagar es:",pagar)



#No olvidar
# for x in range (len(txt)):
# lista=[]
# .append()
# .insert(x,"")
# .pop
# .remove("")
# .reverse()
# .sort()          