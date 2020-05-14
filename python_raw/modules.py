#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Moduły w Pythonie
# Pliki z dołączonymi rozrzerzeniami *.py 

# filepath (sciezka - jako ciąg znaków)
filename = __file__

# Wyznaczamy samą nazwę modułu
try:
    filename = filename.split("\\")[-1].split(".py")[-2]
except IndexError:
    filename = filename.split("\\")[-1]
    print("Nadaj poprawne rozszerzenie " if filename.split(".")[-1]!='py' \
        else 'IndexError in ', end='')
print(filename)

# Jako wartość zmiennej globalnej __name__
print(__name__)     

# 1) Output: '__main__', jezeli dany modul zostanie bezposrednio wywolany 
# 2) Output: 'mod', jezeli modul zostanie posrednio wywolany 
                  
# Moduły - zawierają definicje i instrukcje w języku Python. 


## Cwiczenie importujemy moduly i je wywolujemy 
# Python - zasada importowania (Wykonamy krotkie cwiczenie.)
# Użyj ulubionego edytora tekstu. 
# Utwórz plik o nazwie imo.py w bieżącym katalogu. 
# W imo.py wpisz w pierwszej linii (nie tym razem nie bedzie to shebang line)
# Wyrazenie import i nazwe tego tu modulu, u mnie bedzie to: import mod 
# Napisz ponizej polecenie ktore wypisze __name__.

# Przejdz do docelowego modulu (u mnie mod) i wpisz ponizej 
# import imo

# Teraz Uruchom posrednio i bezposrednio oba moduly. 
# Jaka jest roznica w Outpucie? jakie wartosci przybiera zmienna __name__?

test_if_main = __name__=='__main__'
print(filename + " was executed via import" if test_if_main != True else filename +\
 " was directly executed")


## 
# Importujemy moduly                                                    
# 1) Własne moduły
# 2) Wbudowane biblioteki - W dokumentacji lista dostępnych bibliotek
#   -> https://docs.python.org/3/library/
# 3) System zarządzania pakietami
# ----
# PEP 8
#  - Standard library imports (standardowa bibliotkeka)
#  - Third party imports (moduly zainstalowane gdzies w swojej PYTHONPATH)
#  - Local application imports (wlasne moduly)


#  W Pythonie mamy dwa sposoby importowania modułów. 
# - Bezwzględny import
# - Względny import

# 1.
# Moduły importujemy do swojego programu za pomocą komendy import.
# Najprostszym rodzajem importu, jest import całej biblioteki / modułu. 
# Do tego celu używamy instrukcji o zapisie: import nazwa_biblioteki.

import vars # , b
# Ten typ importu pobiera z biblioteki cala zawartosc
# wszystkie w niej zawarte funkcje, zmienne, klasy.
s_root_9 = vars.foo(9,2)
print(s_root_9)

# 2.
# Jeśli chcemy użyć pojedynczych funkcji z danej biblioteki, 
# to najrozsądniej jest pobrać tylko tą funkcje z ktorej chcemy skorzystac, 
# nie całą zawartość biblioteki. Do tego celu używamy instrukcji: 
# from nazwa_biblioteki import nazwa_pierwszej_funkcji, nazwa_drugiej_funkcji, ...

from vars import rest

reszta_10_2 = rest(10,2)
reszta_10_3 = rest(10,3)

print(reszta_10_2)
print(reszta_10_3)

# zamienne nazewnictwo - alias nazwy modulu, aliasy funkcji
from vars import foo as pierw
print(pierw(16,2))

# Wildcard imports - PEP 8
# Stosowana jest takze instrukcja: from nazwa_biblioteki import * (wszystko)
# należy unikać, ponieważ sprawiają, że nie jest jasne, które nazwy są obecne w przestrzeni nazw, 
# myląc zarówno czytelników, jak i wiele zautomatyzowanych narzędzi.

from vars import *
print(foo(2,2))
print(rest(10,2))


## Importowanie modulow z biblioteki standardowej

print("\n--- calendar ---\n") 

import calendar 
# https://docs.python.org/3/library/calendar.html
# Ten moduł umożliwia wyświetlanie kalendarzy i zapewnia dodatkowe przydatne 
# funkcje związane z kalendarzem. Domyślnie kalendarze te mają poniedziałek 
# jako pierwszy dzień tygodnia, a niedziela jako ostatni (konwencja europejska)

#print(calendar.__all__)
#print(calendar.__doc__)
print(calendar.isleap(2000))


from calendar import isleap, weekday

#print(help(isleap))
print(isleap(2000))
print(weekday(2020,5,8))

print("\n--- datetime & random ---\n") 

from datetime import date as d 
from random import randint
# Moduł random implementuje generatory liczb pseudolosowych dla różnych dystrybucji.
# Moduł datetime dostarcza klasy do manipulowania datami i godzinami.
# https://docs.python.org/3/library/random.html
# https://docs.python.org/3/library/datetime.html

names,l=["Adam","alex","Bartek","mAria","Martin",'tomek','SZYMON', 'ANNA'],[]

for i,val in enumerate(names):
    l.append(randint(2,5))
    print(f"{i}) Dnia {d.today()} {val.capitalize()}\
 otrzymal{'a' if val[-1]=='a' else ''} ocene: \t{l[i] if l[i]>2 else str(l[i])+'*'}")
print("\n   Srednia ocen to:", sum(l)/len(l),"\n")

print("\n--- math ---\n") 

from math import sqrt as pierwiastek, remainder as reszta
# Moduł zapewnia dostęp do funkcji matematycznych określonych przez standard C
# https://docs.python.org/3/library/math.html

print(pierwiastek(9))
print(reszta(9,3))

print("\n--- sys ---\n") 

import sys
# https://docs.python.org/3/library/sys.html
# Moduł sys zapewnia dostęp do niektórych zmiennych używanych lub obsługiwanych przez 
# interpreter oraz funkcji silnie współdziałających z interpreterem.

#print(sys.__doc__)
#print(sys.modules)

# przeiterujmy katalogi przypisane do zmiennej środowiskowej PYTHONPATH, 
# a następnie ścieżki domyślne zależne od instalacji, 
# które są kontrolowane przez moduł lokacji

for p in sys.path:
    print(p)   
# Sprawdzamy w jakim działamy obecnie katalogu, używamy funkcji sys.path[0]
print(sys.path[0])

print("\n--- time & os ---\n") 

import time 
import os
# Moduł time zapewnia różne funkcje związane z czasem. 
# Aby zapoznać się z powiązanymi funkcjami, zobacz także datę i moduły kalendarza
# https://docs.python.org/3/library/time.html

# Ten moduł zapewnia przenośny sposób korzystania z funkcji zależnych od 
# systemu operacyjnego. Jeśli chcesz tylko odczytać lub zapisać plik, zobacz open (), 
# jeśli chcesz manipulować ścieżkami, zobacz moduł os.path, a jeśli chcesz odczytać 
# wszystkie wiersze we wszystkich plikach w wierszu poleceń, zobacz moduł fileinput.
# https://docs.python.org/3/library/os.html

print(dir(os))

# current_dir: funkcja getcwd() - w jakim działamy obecnie katalogu 
current_dir = os.getcwd()
print(current_dir,"\n"*2) 

# mkdir
os.system('mkdir likeinbatch_but_throgh_python'); time.sleep(1)
print("mkdir likeinbatch_but_throgh_python"); time.sleep(1) 
os.system('mkdir likeinbatch_but_stillin_python'); time.sleep(1)
print("mkdir likeinbatch_but_stillin_python\n"); time.sleep(1)
print("\nkoniec tworzenia, teraz pokazmy zawartosc katalogu:", current_dir); time.sleep(1)

# Spowoduje to wydrukowanie kazdego pliku i katalogu w odstepie czasowym 1 sek
for files in os.listdir(current_dir):
    time.sleep(1); print(files)

time.sleep(2); print("\nkoniec, teraz usuwamy katalogi\n"); time.sleep(2)

# rmdir
os.system('rmdir likeinbatch_but_throgh_python'); time.sleep(1)
print("removed likeinbatch_but_throgh_python"); time.sleep(1)
os.system('rmdir likeinbatch_but_stillin_python'); time.sleep(1)
print("removed likeinbatch_but_stillin_python\n"); time.sleep(1)

for files in os.listdir(current_dir):
    time.sleep(1); print(files)

time.sleep(2); print('\nKatalogi zostaly usuniete z folderu:', current_dir); time.sleep(2)



## Importujemy pakiety
# PIP (standard package-management system in Python) - zestaw narzędzi służących do zarządzania napisanymi pakietami 
# automatycznej: instalacji, aktualizacji, konfiguracji i usuwania pakietów oprogramowania.


# https://pypi.org/
# Python Package Index (PyPI) - repozytorium pakietow w Pythonie / Find, install and publish.
# 232,733 projects 1,822,248 releases 2,792,600 files 421,272 users
