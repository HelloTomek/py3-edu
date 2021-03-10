## 0. Komentarze Python

# W programowaniu komentarze są klarownym wyjaśnieniem w kodzie źródłowym programu. 
# Komentarze znajdują się w kodzie źródłowym do czytania przez ludzi po to, aby ułatwić zrozumienie kodu źródłowego. Przeważnie są pomijane przez kompilatory i tłumacze. 


# Pierwszy przykład --> 

# Komentarze w Pythonie zaczynają się od znaku krzyżyka (ang. hash mark), czyli znak # oraz białego znaku i kończą się na końcu linii.
# Python tak naprawdę nie ma składni dla komentarzy wieloliniowych. Aby dodać komentarz wielowierszowy, możesz wstawić # dla każdej linii, lecz ...


# Drugi przyklad -->

"""
W Pythonie zobaczymy wielowierszowe komentarze (komentarze typu multiline). Używany jest w tym celu trzykrotny cudzyslów.

Nie jest to optymalny sposób. Poniżej cytat Guido van Rossum, twórca Pythona: 
>> Python does not support multiline comments like C/C++ or Java. 
>> However there is nothing to stop you to use multi-line docstrings as multiline comments."

Natomiast aby wykomentować skrypt, polecam stosować skróty klawiszowe, np. w IDLE:
- Single line comment. Ctrl + 1.
- Multi-line comment, zaznacz kod który chcesz wykomentować. Ctrl + 4.
- Unblock Multi-line comment. Ctrl + 5.

"""

# Drugi przyklad cd -->

''' 
Spotkamy się także z powyżej stosowaną notacją do wielowierszowych komentarzy - uzywajac pojedynczego cudzysłowu, 

również może być on używany jako docstring, więcej o docstring:
https://www.python.org/dev/peps/pep-0257/

'''


## 1. Zmienne i ich typy

# Zmienne w Pythonie stosuje się do przechowywania wartości dowolnego typu. Utworzenie zmiennej wiąże się z nadaniem jej wartości bazowej (initial value).

## ZMIENNE ZASADY:
#  - W nazwach zmiennych rozróżniana jest wielkość liter (nazwa i NAZWA to różne zmienne).
#  - Muszą one zaczynać się od litery lub znaku podkreślenia.
#  - Nazawa zmiennej może mieć liczby, ale nie może zaczynać się od cyfry.
#  - Zmienne nie mogą nosić takiej samej nazwy jak słowa kluczowe w Pythonie.

# Listę słów kluczowych w aktualnej wersji można zawsze uzyskać, wpisując następujące polecenia:

import keyword
print(keyword.kwlist) # Słowa kluczowe Pythona w formie listy, output:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'


## Utarte normy

# W celu poprawienia czytelności, zrozumiałości kodu programu - nadawanie nazw definiowane jest zgodnie z PEP czyli Python Enhancement Proposal, 
# oficjalnym dokumentem informacyjnym dla społeczności programistów Pythona (URL: https://www.python.org/dev/peps/pep-0008/).

ZacyNAćZwielkich_liter = "To jest niepoprawnie nazwana zmienna" # Błędnie nazwanną zmeinną jest np. zmienna ZacyNAćZwielkich_liter.
nazwazmienna = "To jest poprawnie nazwana zmienna" # Poprawnie: nazwazmienna, ale i nazwa_zmienna, nazwazmienna1, czy nazwa_zmienna_1 jest również poprawnie.

ZacyNAćZwielkich_liter; nazwazmienna # Wykonujemy dwa polecenia Pythona w jednym wierszu.

## 1. a) Typy liczbowe - https://github.com/HelloTomek/IwB/blob/master/python_raw/numbers.py 
## 1. b) Ciągi znaków - https://github.com/HelloTomek/IwB/blob/master/python_raw/strings.py
## 1. c) Listy i tablice -  https://github.com/HelloTomek/IwB/blob/master/python_raw/lists.py
## 1. d) Zbiory i krotki - https://github.com/HelloTomek/IwB/blob/master/python_raw/tuples_sets.py
