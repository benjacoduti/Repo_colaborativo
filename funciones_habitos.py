# Funciones Principales

def analizar_habitos(lista) :
    '''
    Recibe una lista de habitos, cuenta cuantas veces aparece cada habito. Guarda el resultado en un diccionario y devuelve ese diccionario.    

    Parameters
    ----------
    lista : Lista
        Una lista con todos los habitos realizados en un dia

    Returns
    -------
    frequencia : Diccionario
        Key: Habito.
        Value: Frequencia del habito

    '''
    frequencia = {}
    for habito in lista :
        if habito not in frequencia :
            frequencia[habito] = 1
        else :
            frequencia[habito] += 1
    return frequencia

def registrar_habitos():
    terminar = "no"
    lista_de_actividades = []
    while terminar != "si":
        actividades = input("Ingrese las actividades: ")
        lista_de_actividades.append(actividades)
        terminar = input("¿Desea terminar?: ")
    return lista_de_actividades
    
