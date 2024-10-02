import itertools
import datetime
from datetime import time


class Vertesana:
    parbauditaja_v=""
    skolena_v=""
    p_kriterijs=""
    o_kriterijs=""

    id_iter=itertools.count()
    def __init__(self,pad_v=None,skol_v=None,p_k=None,o_k=None):
        self.darbaId =next(self.id_iter)+1
        self.parbauditaja_v = pad_v
        self.skolena_v = skol_v
        self.p_kriterijs = p_k
        self.o_kriterijs = o_k

    def vertesanas_info(self):
        return [self.parbauditaja_v,self.skolena_v,self.p_kriterijs,self.o_kriterijs]
        
    def vertesana_info_print(self):
        print("Parbauditaja vards:"+ str(self.parbauditaja_v))
        print("Skolena vards:"+str(self.skolena_v))
        print("pirmais kriterijs:"+str(self.p_kriterijs))
        print("otrais kriterijs:"+str(self.o_kriterijs))

ver1=Vertesana("Marija","Aleksejs","Saturs","Struptura")
print(ver1.darbaId)
ver1.vertesanas_info()
ver1.vertesana_info_print()
