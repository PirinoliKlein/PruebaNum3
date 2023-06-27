import Funciones as fn


while True:
    print("""Bienvenido a Mascota Segura
    1- Grabar datos
    2- Buscar mascota
    3- Retirarse(Pagar)
    4- Salir""")

    opc=fn.validad_opc()

    if opc==1:
        fn.validar_rut()
        fn.validar_nombre()
        fn.validar_mascota_nom()
        fn.validar_cantidad()
        fn.validar_habitacion()
        print("Sus datos de usted y su mascota se registraron exito!")
    elif opc==2:
        fn.buscar_rut()
    elif opc==3:
        fn.total_pagar()
    else:
        break
    print("Gracias por su visita, vuelva pronto!")
