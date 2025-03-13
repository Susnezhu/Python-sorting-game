#Pelin koodi kirjoitetaan tähän
import pygame

pygame.init()

from kuvien_lataus import * #tiedosto, jossa on kaikki kuvat
from peli_objektit import * #tiedosto, jossa on luokka PeliObjektit

LEVEYS = 900
KORKEUS = 600
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Roskien lajittelu peli")



while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x, y = tapahtuma.pos
            for obj in objektit:
                if obj.reunat.collidepoint(x, y):
                    print("object found") #tähän pitää lisätä hiiren seuraaminen
                    print(obj.arvo) #kertoo mihin roskikseen se menee


        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.blit(taustakuva, (0,0))
    for objekti in objektit:
        objekti.lisaa(naytto)
    

    naytto.blit(kartonki_roskakori, (500, 260))
    naytto.blit(bio_roskakori, (700,260))
    naytto.blit(lasi_roskakori, (100, 200))
    naytto.blit(metalli_roskakori, (300, 200))
    naytto.blit(muovi_roskakori, (600, 270))
    naytto.blit(paperi_roskakori, (200, 200))
        
    pygame.display.flip()