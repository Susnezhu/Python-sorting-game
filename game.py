#Pelin koodi kirjoitetaan tähän
import pygame

pygame.init()

from kuvien_lataus import * #tiedosto, jossa on kaikki kuvat

LEVEYS = 900
KORKEUS = 700
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Roskien lajittelu peli")


#eri roska ryhmien listat ja oliona kuvat
paperi = [piirustus, sanomalehti, kirjekuori]
kartonki = [paperikassi, munakeno, maitopurkki]
muovi = [muovipussi,saippua, muovipullo]
lasi = [lasipullo,lasipurkki]
bio = [omena, kalaruodot, kukat]
metalli = [kattila, ananaspurkki]

class Roskat:
    def __init__(self):
        self.paperi = []
        self.kartonki = []
        self.muovi = []
        self.lasi = []
        self.biojate = []
        self.metalli = []
    def lisaa(self, lista, arvo):
        if arvo == 1:
            self.paperi = lista
        elif arvo == 2:
            self.kartonki = lista
        elif arvo == 3:
            self.muovi = lista
        elif arvo == 4:
            self.lasi = lista
        elif arvo == 5:
            self.biojate = lista
        elif arvo == 6:
            self.metalli = lista
    def __str__(self):
        return f"{self.paperi}, {self.kartonki}, {self.muovi}, {self.lasi}, {self.biojate}, {self.metalli}"

roskat = Roskat()
roskat.lisaa(paperi,1)
roskat.lisaa(kartonki,2)
roskat.lisaa(muovi,3)
roskat.lisaa(lasi,4)
roskat.lisaa(bio,5)
roskat.lisaa(metalli,6)

nelio = pygame

print(roskat)

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.blit(taustakuva, (0,0))

    pygame.display.flip()