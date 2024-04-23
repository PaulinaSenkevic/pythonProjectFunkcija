print('------16 tema------')
def pasisveikinti():
    print('labas krabas')

pasisveikinti()

def eilerastis():
    print('labas rytas')
    print ('su peleda')
eilerastis()
eilerastis()
eilerastis()

pasisveikinti()
eilerastis()

print('------1 uzduotis-----')
def apieMane():
    print('Paulina')
    print('del ziniu')

apieMane()
apieMane()
apieMane()

print('------2 uzduotis-----')
def eilerastis():
    print('Sniegena, smegenėle,\nVai kas tau pasiuvo \nTokią raudoną prijuostėlę? \nKaip šermukšnio uogą, \nKaip rožės lapelį,\nKaip aušros spindulėlį?')
eilerastis()
eilerastis()
eilerastis()
eilerastis()
eilerastis()

print('------3 uzduotis-----')

def pasisveikinimas():
    print('sveiki')
def atsisveikinimas():
    print('viso gero')
def abu():
    print('labas ir ate')

pasisveikinimas()
atsisveikinimas()
abu()

print('------4 uzduotis-----')
def spalva():
    print('raudona')
def vaisius():
    print('braske')

def maistas():
    spalva()
    vaisius()

maistas()
print('------5 uzduotis-----')
import random

def numbers():
    sk1 = random.randint(10, 20)
    sk2 = random.randint(1, 10)
    suma = sk1 + sk2
    print(f'{sk1} + {sk2} = {suma}')
numbers()
numbers()
numbers()

print('------6 uzduotis-----')
def policininko_info(vardas, pavarde, amzius, alga, etatas, specializacija):
    print(f'vardas: {vardas}')
    print(f'pavarde: {pavarde}')
    print(f'amzius: {amzius}')
    print(f'alga: {alga}')
    print(f'etatas: {etatas}')
    print(f'specializacija: {specializacija}')
# vardas = 'Tomas'
# pavarde = 'Tomaitis'
# amzius = 30
# alga = 1500
# etatas = 'Pilnas'
# specializacija = 'keliu policininkas'
policininko_info(vardas='Tomas', pavarde='Tomaitis', amzius=30 ,alga=1500, etatas='Pilnas', specializacija='keliu poliininkas')

print('------7 uzduotis-----')
def rnd():
    sk = random.randint(0,100)
    print(sk)
    print()
for a in range(5):
    for i in range(10):
      rnd()
rnd()

print('------8 uzduotis-----')
# def randomSk():
#     a = random.randint(1,10)
#     return(a)
#
# for i in range(10):
#     print(randomSk())

print('------9 uzduotis-----')

def pasisveikiti(vardas):
    print('labas', vardas)
def atsisveikinti(vardas):
    print('viso gero', vardas)
vardas = 'Justas'

pasisveikiti(vardas)
atsisveikinti(vardas)

print('------10 uzduotis-----')
def skaiciai(sk1, sk2):
    if sk1 > sk2:
        print('skaicius 1 yra didesnis uz 2 skaiciu')
    if sk2 > sk1:
        print('skaicius 2 yra didesni uz skaiciu 1')
    if sk1 == sk2:
        print('skaiciai yra lygus')

sk1 = 78
sk2 = 999
skaiciai(sk1, sk2)

print('------12 uzduotis-----')
def suma(sk1, sk2):
    print(f'{sk1} + {sk2} =', sk1 + sk2)
def skirtumas(sk1, sk2):
    print(f'{sk1} - {sk2} =', sk1 - sk2)

def sandauga(sk1, sk2):
    print(f'{sk1} * {sk2} =', sk1 * sk2)
def dalmenis(sk1, sk2):
    print(f'{sk1} / {sk2} =', sk1 / sk2)

def funkcija(sk1, sk2):
    sk1 = random.randint(1, 10)
    sk2 = random.randint(1, 10)
    suma(sk1, sk2)
    skirtumas(sk1, sk2)
    dalmenis(sk1, sk2)
    sandauga(sk1, sk2)

funkcija(sk1, sk2)

print('------11 uzduotis-----')
# Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis (markė, modelis, gamybos metai, darbinis tūris).
# Ši funkcija turėtų šiuosduomenis išvesti kaip nors gražiai formatuotai. Iškvieskite šią funkciją du
# kartus, perduodant skirtingus duomenis jai.

def automobilis(marke, modelis, metai, turis):
    print(f'marke: {marke}')
    print(f'modelis: {modelis}')
    print(f'metai: {metai}')
    print(f'turis: {turis}')
def automobilisOne(marke, modelis, metai, turis):
    print(f'Parduodamas automobilis {marke}, kurio modelis yra {modelis}. Automobilis yra beveik naujas, {metai} gamybos.Automobilio variklio turis yra {turis} litrai')

automobilis(marke='BMW', modelis='X7', metai =2020, turis=3 )
print()
automobilis(marke='Audi', modelis='Q7', metai =2018, turis=3 )
print()
automobilisOne(marke='BMW', modelis='X7', metai =2020, turis=3 )
print()
automobilisOne(marke='Audi', modelis='Q7', metai =2018, turis=3 )

print('------13 uzduotis-----')
# Susikurkite funkciją, kuri per argumentus priimtų žodžių masyvą.
# Funkcijoje išveskite visus žodžius iš masyvo atskirose eilutėse,
# nurodant žodžio ilgį (simbolių kiekį).
# Už funkcijos ribų susikurkite žodžių masyvą ir
# užpildykite jį duomenimis.
# Iškvieskite sukurtą funkciją perduodant turimą masyvą.

def isvesti_masyva(komentaras, masyvas):
    print(komentaras)
    for elementas in masyvas:
        print('-', elementas)
    print()
skaiciai = [8, 7, 9]
zmones = ['Asta', 'Inga', 'Giedrius', 'Justas']
isvesti_masyva('Skaiciai', skaiciai)
isvesti_masyva('Zmones', zmones)
