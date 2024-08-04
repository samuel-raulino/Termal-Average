from SimpleFile import * 
from __random import *
class Avarage:
    def __init__(self,pais):
        self.temperaturas = File("temperaturas")
        self.temperaturas.create()
        self.pais = pais 
        self.minverao = ""
        self.maxverao = ""
        self.mininv = ""
        self.maxinv = ""
    
    def make_avarage(self):
        for x in range(1,len(self.temperaturas.all_lines())+1):
            lista = self.temperaturas.read_line(x)
            lista = lista.split()
            if self.pais in lista:
                self.maxinv = self.temperaturas.read_line(x+2)
                self.mininv = self.temperaturas.read_line(x+3)
                self.maxverao = self.temperaturas.read_line(x+5)
                self.minverao = self.temperaturas.read_line(x+6)
                
                break
            if x == len(self.temperaturas.all_lines()):
                print("pais não encontrado")
        mudanca = ""
        for x in self.maxinv:
            if x in ["-","0","1","2","3","4","5","6","7","8","9"]:
                mudanca +=x 

        self.maxinv = int(mudanca)
        mudanca = ""
        for x in self.mininv:
            if x in ["-","0","1","2","3","4","5","6","7","8","9"]:
                mudanca +=x 

        self.mininv = int(mudanca)
        mudanca = ""
        for x in self.maxverao:
            if x in ["-","0","1","2","3","4","5","6","7","8","9"]:
                mudanca +=x 

        self.maxverao = int(mudanca)
        print(self.maxverao)
        mudanca = ""
        for x in self.minverao:
            if x in ["-","0","1","2","3","4","5","6","7","8","9"]:
                mudanca +=x 

        self.minverao = int(mudanca)
        