#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:52:28 2026

@author: ramiroyoffe
"""

def analizar_habitos(lista) :
    '''
    Recibe una lista de habitos, cuenta cuantas veces aparece cada habito. Guarda el resultado en un diccionario y devuelve ese diccionario.    

    Parameters
    ----------
    lista : Lista
        Una lista con todos los habitos realizados en un dia

    Returns
    -------
    frequencia : DIccionario
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