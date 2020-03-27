## Ciągi znaków w Pythonie 
# Ciągi znaków w pythonie są otoczone pojedynczymi lub podwójnymi cudzysłowami. Spójrzmy na formatowanie ciągów i niektóre metody na danych typu String.
# typ sekwencyjny - w jednej zmiennej możemy przechować wiele wartości
# String-data w Pythonie są niemutowalne (niezmienne)

# 1. Wpisz swoje dane ✍

nickname = 'Hello *Tu podaj swoje imie*'
age = 20

print(nickname)
print(age)
#print(nickname, age)

# Print zakończony jest „niewidzialnym” znakiem nowej linii (\n), mozemy sie od tego uwolnić

print(nickname, end='')
#print('Tomek, ', end=' ')
print(age)

# sprawdzamy typ obu zmiennych
# zauwazamy ze zmienna wiek jest typu int

print(type(nickname), type(age))

## Formatowanie ciągów znaków

# 2. Wyznacz imie ze swojego nicku i napisz powitanie uwzgledniając wiek ✍

# nalezy utworzyć nowa zmienną, nadać nazwę "name", 
# aby przypisac wartość, skorzystaj z funkcji split pozwoli ona nam rozszcepic napis na pojedyncze człony.
# split(str="", num=string.count(str)) # - dzieli napis według separatora str (spacja jeśli nie podano) i zwraca podciągi jako listę.
# splitlines( num=string.count('n')) # - dzieli napis (lub wg zadanej liczby num) na osobne linie wg znaku nowej linii’\n’ i zwraca je jako listę. 


name ='To Do'

## Konkatencja - w programowaniu oznacza łączenie dwóch wyrażeń 
# Zastosowana została funkcja kastowania (casting to string), inaczej konwersji tzpu danych
# by moc polaczyc dwa rozne wartosci o roznych typach danych.

print('Witajcie, mam na imie ' + name + ' i mam ' + str(age) + ' lat')

# R- & F-Strings (3.6+)
# Natomiast w ostatnim, za pomocą ukośnika \ zaznaczamy, że ' jest znakiem specjalnym  
# Mówiąc językiem programistów: escapujemy za pomocą backslasha

print(f'No i yahoo, ja tez jestem {name}, \nmam {age} lat')
print(R'a ja jestem raw {name}, \nmam {age} lat')
#O! Mamy nowy błąd! Nie chcemy zeby tak to wygladało 😀 zastosuj notacje fr'napis' ✍

# Argumenty pozycyjne
hi = ("Hey I'm {imie}, mam wlasnie {wiek} lat".format(imie=name, wiek=age))

## Metody stosowane na ciągach znaków 
# 3. Wypełnij kodem (dopisz napisy, ktore sa watośćiami zmiennych, nazwij poprawnie zmienne ✍)
# Stosuj zrozumiale i praktyczne nazewnictwo
# Stosowana notacja: (''), (""), (''' '''), (""" """")

status = '''  HOME OFFICE  '''
_profile_img =''
me_about_hobby = ''
me_about_job = ""
me_about_motivation = """"""

me_about_motivation_r = r"""Give me six hours to chop down a tree\nand I will spend the first four sharpening the axe."""

## Modyfikacja napisow 

# Rozbierz napis, np. usuń "zbedne" spacje na początku i na końcu oraz make all lowercase (✍)

_status =''

# print(_status)

# SUPER! Teraz uruchom kod, przetestuj się czy oczekiwałeś takiego rezultatu? ✍

# Make all uppercase
print(me_about_job.upper())

# Napis typu tytul
print(me_about_motivation.title())

# Zmienia pierwszą literę w ciągu na dużą
print(me_about_hobby.capitalize())

# Odwraca rodzaj każdej litery – małe na duże, duże na małe
print(me_about_motivation_r.swapcase())

# Zamienia znak/znaki
print(name.replace('Tomek', 'everyone'))

# string slicing - ciecie napisow
print(me_about_motivation_r[4:-4])

# Output boolean type - poczatek sekwencji znakow
print(_status.startswith('office'))

# Output boolean type - koniec sekwencji znakow
print(name.endswith('k'))

# Output int - zmierz dlugosc
print(len(name))

# Output int - zlicz ile razy wystepuje nasz substring w napisie
sub = 'e'
print(me_about_job.count(sub))

# rozszczepiamy napis do listy
print(me_about_hobby.split(','))

# Znajdz pozycje
print(name.find('e'))

# Output boolean type - Is all alphanumeric
print(name.isalnum())

# Output boolean type - Is all alphabetic
print(str(age).isalpha())

# Output boolean type - Is all numeric
print(str(age).isnumeric())

