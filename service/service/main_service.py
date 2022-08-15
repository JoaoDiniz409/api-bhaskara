import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd



class BhaskaraService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)

    def calculate_roots(self, object:dict):
        a = object["a"] 
        b = object["b"] 
        c = object["c"]

        if a == 0:
            return {"message": "Parâmetro 'a' não pode ser 0"}
        


        return self.__bhaskara(a, b, c)

    def __bhaskara(self, a:float, b:float, c:float):
        # resolver uma equacoes do segudo grau:
        # ax^2+bx+c = 0

        # delta = b^2 - 4ac
        delta = b**2 - 4*a*c

        if delta < 0:
            return {"message": "A equação não tem valores reais"}

        # X = (-b +- raiz(delta))/2a
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)

        return { "x1" : x1, "x2": x2}





