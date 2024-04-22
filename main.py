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

sk1 = random.randint(1, 10)
sk2 = random.randint(1, 10)
for i in range(4):
    suma(sk1, sk2)