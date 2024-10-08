import itertools
import datetime
from datetime import time


class Vertesana:
    parbauditaja_v=""
    skolena_v=""
    prieksmets=""

    
    id_iter=itertools.count()
    def __init__(self,pad_v=None,skol_v=None,priek=None,):
        self.darbaId =next(self.id_iter)+1
        self.parbauditaja_v = pad_v
        self.skolena_v = skol_v
        self.prieksmets = priek

    def vertesanas_info(self):
        return [self.parbauditaja_v,self.skolena_v,self.prieksmets]
        
    def vertesana_info_print(self):
        print("Parbauditaja vards:"+ str(self.parbauditaja_v))
        print("Skolena vards:"+str(self.skolena_v))
        print("Priekšmets:"+str(self.prieksmets))
        

class Krit:
    p_kriterijs=""
    o_kriterijs=""
    t_kriterijs=""
    id_iter_k1=itertools.count()
    def __init__(self,p_k,o_k,t_k):
        self.p_kriterijs = p_k
        self.o_kriterijs = o_k
        self.t_kriterijs = t_k
    def krit_info(self):
        print("Pirmais kriterijs:"+self.p_kriterijs)
        print("otrais kriterijs:"+ self.o_kriterijs)
        print("trešāis kriterijs:"+self.t_kriterijs)

ver1=Vertesana("Marija","Aleksejs","priogrammešāna")
ver2=Vertesana("Aleksandrs","Mihail","Angļu valoda")
ver3=Vertesana("Emma","Ksenija","Latviešu valoda")
print(ver1.darbaId)
ver1.vertesanas_info()
ver1.vertesana_info_print()
print(ver2.darbaId)
ver2.vertesanas_info()
ver2.vertesana_info_print()
print(ver3.darbaId)
ver3.vertesanas_info()
ver3.vertesana_info_print()
#https://github.com/M4rakesh/uzd/blob/main/mechta.py