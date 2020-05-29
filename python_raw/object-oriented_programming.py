#!/usr/bin/python3 
# -*- coding: utf-8 -*-

# Elementy programowania obiektowego
# Klasy w Pythonie - schemat, według którego tworzone są obiekty.
# Połączenie danych i funkcji, które na nich operują, 
# np. klasę łańcuchów znakowych -> str(s), len(s)

# Tworzymy wlasne klasy
# Struktura klasy:

"""
class NazwaKlasy (KlasyBazowe):
	konstruktor
	lista_metod
"""

# Nazwa klasy - System notacji ciągów tekstowych: CapWords, (CamelCase)
# https://www.python.org/dev/peps/pep-0008/#class-names
   
class PustaKlasa:
    pass

print('\n',"PustaKlasa".center(35, '-'),'\n')
print(PustaKlasa.__doc__)


print('\n',"KoloJeden".center(35, '-'),'\n')


class KoloJeden(object):
    """Klasa: KoloJeden 
    Posiadajaca docstring; 
    atrybuty pi i r."""
    pi = 3.14
    r = 10
    
print(KoloJeden.__doc__)
print(KoloJeden.pi)
print(KoloJeden.r)

print ('\n','Tworzymy obiekt: kolo_fortuny'.center(35, '-'),'\n')

# Obiekt - instancja danej klasy; obiekt: kolo_fortuny
# Wywolany zostanie konstruktor klasy: KoloJeden().
kolo_fortuny = KoloJeden()
print('pi = ', kolo_fortuny.pi)

# Konstruktor może zawierać inicjalizację wartości zmiennych klasowych 
# - danych przypisanych do klasy 


print('\n', "KoloDwa".center(35, '-'),'\n')


# Klasa bez zdefiniowanego konstruktora nie może przyjmować parametrów. 
# Wprowadzamy funkcje __init__, która może przyjmować parametry.

# Zdefiniujmy klasę KoloDwa, posiadac ona bedzie przypisana zmienna klasowa pi.
# W klasie znajduje sie kod konstruktora __init__, 
# pozwala on na podanie zmiennych inicjacyjnych obiektu.
# Do klasy KoloDwa dopisano metody: obwod(), pole(), pojemnosc_kola(). 

class KoloDwa:   
    """Klasa KoloDwa    
    atrybut pi = 3.14

    Constructor arguments:
    :param r: promien od srodka kola float(r)
    :param h: szerokosc kola float(h) 
    """
    pi = 3.14
    
    def __init__(self, r, h):
        self.r = float(r)
        self.h = float(h)

    def obwod(self):
        return 2 * self.pi * self.r
        
    def pole(self):
        return self.pi * self.r ** 2
    
    def pojemnosc_kola(self):
        return KoloDwa.pole(self)*self.h


# Zmienna instancji należy do obiektu
kolo_zapas_audi_a4 = KoloDwa(32, 20)
kolo_zapas_fiat_126p = KoloDwa( 27, 18)

poj_kolo_zapas_audi_a4 = kolo_zapas_audi_a4.pojemnosc_kola()
poj_kolo_zapas_fiat_126p = kolo_zapas_fiat_126p.pojemnosc_kola()

# Obliczamy miejsce na kolo zapasowe pojemnosc i wynik podajemy w litrach
print("Wyk. msc. na kolo zapasowe, w audi a4 pomiesci ", end='')
print(str(round(poj_kolo_zapas_audi_a4)/1000/2), 'litrow gazu')

print("Wyk. msc. na kolo zapasowe, w 'maluchu' pomiesci ", end='')
print(str(round(poj_kolo_zapas_fiat_126p)/1000/2), 'litrow gazu')

# Wyświetlanie zawartości obiektu (bez uzycia metody __str__)
print(kolo_zapas_audi_a4) # generuje napis <__main__.KoloDwa object at ... >

print('\n', "KoloTrzy".center(35, '-'),'\n')

# Kolo trzy posiada konstruktor pozwalający na 
# podanie długości promienia i zmiennej pi 
# oraz metodami :obwod(), pole(), pojemnosc_kola() 
# metoda pojemnosc_kola() przyjmuje parametr zewnetrzny (nie od konstruktora).

class KoloTrzy:
    """Klasa KoloTrzy 

    Constructor arguments:
    :param pi: float(pi) 
    :param r: promien od srodka kola float(r)
    """
    pi = 3.14
    r = 10

    def __init__(self, pi, r):
        self.pi = float(pi)
        self.r = float(r)

    def obwod(self): # , r):
        return 2 * self.pi * self.r
        # return 2 * math.pi * self.r
        
    def pole(self):
        return self.pi * self.r ** 2
        # return math.pi * self.r ** 2
    
    def pojemnosc_kola(self, h):
        return KoloDwa.pole(self) * h
    
    def __str__(self):
        # Wyswietlamy zawrtosc obiektu
        return 'zmienna instancji pi to ma wartosc ('+str(self.pi)+')'

# pobieramy wartosc (z funkcji) pi z biblioteki standardowej math
from math import pi
# zmienna klasowa nadal ma oryginalną wartość 3.14 
print("zmienna klasowa", pi)
print("zmienna instancji obiektu", KoloTrzy.pi)

# metoda __init__ ustawia wartość zmiennej instancji pi na math.pi
kolo_zapas_audi_a4 = KoloTrzy(pi, 32)
kolo_zapas_fiat_126p = KoloTrzy(pi, 27)

poj_kolo_zapas_audi_a4 = kolo_zapas_audi_a4.pojemnosc_kola(20.0)
poj_kolo_zapas_fiat_126p = kolo_zapas_fiat_126p.pojemnosc_kola(18.0)
#kolo_zapas_audi_a4.pojemnosc_kola(20)

# obliczamy miejsce na kolo zapasowe pojemnosc i wynik podajemy w litrach
print("kolo zapasowe, w audi a4 pomiesci ", end='')
print(str(round(poj_kolo_zapas_audi_a4)/1000/2), 'litrow gazu')

print("kolo zapasowe, w 'maluchu' pomiesci ", end='')
print(str(round(poj_kolo_zapas_fiat_126p)/1000/2), 'litrow gazu')

# Efekt uzycia metody __str__ 
# (porownaj z instancja klasy KoloDwa)
# Wyświetlanie zawartości obiektu kolo_zapas_audi_a4 (wskazuje na metode __str__)
print(kolo_zapas_audi_a4) # właściwy rezultat


print('\n',"Modyfikujemy wartosc pi".center(55, '-'),'\n')


# Pola obiektów mogą być dowolnie modyfikowane przez kod spoza klasy, 
# co może prowadzić do błędów wykonania lub semantycznych:
# Przykladowo modyfikujemy wartosc pi w zmiennej klasowej.

change_obj = KoloDwa
change_obj.pi='7'
print(f"Zmienna klasowa pi w klasie KoloDwa posiada nowa wartosc: {KoloDwa.pi}\n")

kolo_zapas_bmw_120i = KoloDwa(30,20)

# Jezeli bedziemy chcieli obliczyc wartosc, otrzymamy 
# Error: TypeError
# can't multiply sequence by non-int of type 'float' 
# Przetestuj, odkomentuj ponizsza linie kodu: 
#poj_kolo_zapas_bmw_120i = kolo_zapas_bmw_120i.pojemnosc_kola()

# zmienmy typ danych, lecz wartosc nadpiszmy bledna wartoscia
change_obj.pi= 9.14
print(f"Zmienna klasowa pi w klasie KoloDwa posiada nowa wartosc: {KoloDwa.pi}")
poj_kolo_zapas_bmw_120i = kolo_zapas_bmw_120i.pojemnosc_kola()

print("Wyk. msc. na kolo zapasowe, w BMW 120i pomiesci ", end='')
print(str(round(poj_kolo_zapas_bmw_120i)/1000/2), 'litrow gazu')


print('\n', "NiedostepneZmienne".center(35, '-'),'\n')

## Hermetyzacja (enkapsulacja danych) 
# Definiujemy dostępnosc pewnych danych składowych lub metod obiektów danej klasy. 
# Wskazane jest umowne ukrycie pól poprzez dodanie _ z przodu ich nazwy. 
# Nazwa zaczynająca się od  __ (dwóch znaków jest niedostępna), natomiast jest widoczna 
# dla metod wewnętrznych danej klasy lub funkcji zaprzyjaźnionych.


class NiedostepneZmienne:
    _prywatna = 1
    __prywatna = 2
    
    def pp(self):
        print(self._prywatna)
    
    def pp2(self):
        print(self.__prywatna)

t = NiedostepneZmienne()
t.pp()
print(t._prywatna)
print("---")
t.pp2()
#print(t.__prywatna)  #<-- Usun komentarz (otrzymamy AttributeError)

# Natomiast Python nie umozliwia nam "prawdziwego" zabezpieczania,
# poniewaz mamy mozliwość odwołania się do "niedostepnej" zmiennej klasowej __prywatna,
# zastosujemy trick:
print(t._NiedostepneZmienne__prywatna)

# Rownież używanie dekoratorów jest formą zabezpieczania atrybutów czy metod, stosuje się: 
# > gettera funkcji - zwracającej wartość pola (dekorator @property)
# > settera funkcji - pozwalającej zmienić wartość (dekorator @setter)


print('\n',"Dziedziczenie".center(35, ' '))
print("KoloCztery (KoloDwa)".center(35, '-'),'\n')


## Dziedziczenie klas (dodajemy KlasyBazowe)
# Dziedziczenie pozwala wykorzystać w definicji klasy inną istniejącą już klasę

class KoloCztery(KoloDwa):
    pass

print(KoloCztery.pi)
# Otrzymujemy klasy pochodne


print('\n', "Dziedziczenie (Samochod)".center(35, '-'),'\n')


# Klasa matka Samochod 
class Samochod:
    def __init__(self, marka, kolor):
        self.marka = marka
        self.kolor = kolor
    
    def __str__(self):
        return self.marka + ' w kolorze: ' + self.kolor

# Klasa Tapicerka dziedziczy od klasy bazowej Samochod
class Tapicerka(Samochod):
    def skorzana(self):
        return self.kolor == 'bialy'

class Podsufitka(Samochod):
    def szyberdach(self):
        return self.kolor == 'szklany'

# Tworzymy obiekty
car = Samochod('Volvo','czarny')
roof = Podsufitka('Podsufitka pikowana','szklany')
interior = Tapicerka('skóra','bialy')

# obiekty klas Tapicerka i Podsufitka należą jednocześnie do klasy Samochod, 
# dlatego konstruktora i metody __str__ można używać dla każdego z nich
print(car, interior, roof, sep='\n')

# metoda skorzana zdefiniowana jest tylko dla klasy Tapicerka i 
# tylko dla obiektów tej klasy można jej używać
print(interior.skorzana()) # True
#roof.skorzana() #<-- AttributeError 'Podsufitka' object has no attribute 'skorzana'

# metoda szyberdach zdefiniowana jest tylko dla klasy Podsufitka 
# i tylko dla obiektów tej klasy można jej używać
print(roof.szyberdach()) # True
#roof.letnie() #<-- AttributeError 


print('\n', "Tapicerka2 (Samochod)".center(35, '-'),'\n')


# Jezeli chcemy odwolac sie z metody przeciążanej do metody bazowej o tej samej nazwie. 
# Można to zrobić uzywajac funkcji super zwracającej klasę nadrzędną.

class Tapicerka2(Samochod):

    #Przykładowo, metodę __init__ klasy Tapicerka można zapisac w poniższej formie
    def __init__(self, material='skóra', kolor='bialy'):
        super().__init__(material, kolor)
        # Nie wpłynie to na jej działanie:

    def skorzana(self):
        return self.kolor == 'bialy'

t = Tapicerka2()
print(t)  # skóra w kolorze: bialy


print('\n', "Dziedziczenie wielokrotne".center(35, '-'),'\n')


##Klasy mogą dziedziczyć po więcej niż jednej klasie bazowej. 
# Przykładowo klasa Student dziedziczy jednocześnie po klasach Osoba i Oceny

class Osoba:
    imie = "Anna"
    nazwisko = "Kowalska"    
 
class Oceny:
    termin1 = {"Ekonomia": 3, "Programowanie komputerow": 2}
    termin2 = {"Programowanie komputerow": 5}

    def zaliczenie(self, p):
        return self.termin1[p] if self.termin1[p] > 2 else self.termin2[p] 

class Student(Osoba, Oceny):
    kierunek = "Informatyka w Biznesie"

# W klasie pochodnej można używać pól i metod obu klas bazowych
s = Student()
print(s.imie, s.nazwisko, s.zaliczenie("Programowanie komputerow"))
