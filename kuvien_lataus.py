#Tämä tiedosto lataa kaikki kuvat ja tallentaa niitä
import pygame

def lataa_kuva(nimi:str):
    return pygame.image.load(nimi)

taustakuva = lataa_kuva("kuvat/background.png")
kulta = lataa_kuva("kuvat/kultamitali.png")
pronssi = lataa_kuva("kuvat/bronze_mitali.png")
hopea = lataa_kuva("kuvat/silver_mitali.png")

#roskakorit
bio_roskakori = lataa_kuva("kuvat/bio_roskakori.png")
kartonki_roskakori = lataa_kuva("kuvat/kartonki_roskakori.png")
lasi_roskakori = lataa_kuva("kuvat/lasi_roskakori.png")
metalli_roskakori = lataa_kuva("kuvat/metalli_roskakori.png")
muovi_roskakori = lataa_kuva("kuvat/muovi_roskakori.png")
paperi_roskakori = lataa_kuva("kuvat/paperi_roskakori.png")

#roskat
piirustus = lataa_kuva("kuvat/piirustus.png")
sanomalehti = lataa_kuva("kuvat/sanomalehti.png")
kirjekuori = lataa_kuva("kuvat/kirjekuori.png")

paperikassi = lataa_kuva("kuvat/paperikassi.png")
munakeno = lataa_kuva("kuvat/munakeno.png")
maitopurkki = lataa_kuva("kuvat/maitopurkki.png")

muovipussi = lataa_kuva("kuvat/muovipussi.png")
saippua = lataa_kuva("kuvat/saippua.png")
muovipullo = lataa_kuva("kuvat/muovipullo.png")

lasipullo = lataa_kuva("kuvat/lasipullo.png")
lasipurkki = lataa_kuva("kuvat/lasipurkki.png")

omena = lataa_kuva("kuvat/omena.png")
kalaruodot = lataa_kuva("kuvat/kalaruodot.png")
kukat = lataa_kuva("kuvat/kukat.png")

kattila = lataa_kuva("kuvat/kattila.png")
ananaspurkki = lataa_kuva("kuvat/ananaspurkki.png")


#ryhmitetys roskat listoissa
paperi = [piirustus, sanomalehti, kirjekuori]
kartonki = [paperikassi, munakeno, maitopurkki]
muovi = [muovipussi,saippua, muovipullo]
lasi = [lasipullo,lasipurkki]
bio = [omena, kalaruodot, kukat]
metalli = [kattila, ananaspurkki]
