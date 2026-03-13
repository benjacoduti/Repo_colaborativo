def registrar_habitos():
    terminar = "no"
    lista_de_actividades = []
    while terminar == "no":
        actividades = input("ingrese las actividades:")
        lista_de_actividades.append(actividades)
        terminar = input("desea continuar:")