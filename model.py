STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'w'
PORAZ = 'x'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crke = [] if crke == None else crke  #to je pogojni IZRAZ!!!!!!!!!!!!!!
    
    def napacne_crke(self):
        napacne = []
        for crka in crka:
            if crka not in self.geslo:
                napacne.append(crka)
        return napacne

    def pravilne_crke(self):
        pravilne = []
        for crka in crka:
            if crka in self.geslo:
                pravilne.append(crka)
        return pravilne

    def stevilo_napak(self):
        return len(napacne)

    def zmaga(self):
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                return 'Zmaga!'
    
    def poraz(self):
        if stevilo_napak() >= 10:
            return True
        else:
            return False
        

    def pravilni_del_gesla(self):
        nova_beseda = ''
        for crka in self.geslo:
            if crka in self.crka():
                nova_beseda += crka + ' '
            else:
                nova_beseda += ' _ '
        return nova_beseda

    def nepravilni_ugibi(self):
        nepravilni_ugibi = ''
        for crka in self.geslo:
            if crka in self.napacne_crke():
                nepravilni_ugibi += crka + ' '
        return nepravilni_ugibi

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka not in self.geslo:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
        else:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA

bazen_besed = []    
with open('besede.txt', 'r', encoding='utf-8') as f:
    for vrstica in f:
        bazen_besed.append(vrstica)

import random
def nova_igra():
    return Igra(random.choice(bazen_besed))



    



