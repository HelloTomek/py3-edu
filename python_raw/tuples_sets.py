#!/usr/bin/python3

## TUPLES - KROTKA
## Tworzymy krotki
# Link do dokumentacji https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# Krotka (Tuple) to kolekcja, która jest uporządkowana i niezmienna. Umożliwia duplikaty elementów,
# krotki w odroznieniu od list są niezmiennymi sekwencjami i zwykle stosowanymi do przechowywania rożnorodnych zbiorów danych.
# Zapis krotek odbywa sie za pomoca nawiasow okraglych, jak i rowniez w przypadku "tuple3" mozemy utworzyc tuple bez użycia nawiasu.

tuple0 = ()                     # Tworzymy pustą krotkę
tuple1 = ('Python', 1989, 'Java', 1996)
tuple2 = (1, 2, 3, 4, 5 )
tuple3 = "a", "b", "c", "d"
tuple4 = 'Prolog',              # Zwróćmy uwagę na przecinek na końcu wiersza
tuple5 = tuple('krotka')

print(tuple5)                   # Output "('k', 'r', 'o', 't', 'k', 'a')"

tup1 = tuple1, tuple2, tuple3   # Nowy twór (krotka) składajacy sie z 3 odrębnych subkrotek
print(tup1)                     # Output "(('Python', 1989, 'Java', 1996), (1, 2, 3, 4, 5), ('a', 'b', 'c', 'd'))"

## Konkatenacja krotek 
tup2 = tuple1+tuple2+tuple3     # Nowy twór (krotka) składajacy się ze zlepka 3 krotek
print(tup2)                     # Output "('Python', 1989, 'Java', 1996, 1, 2, 3, 4, 5)"

# Dostęp do elementów odbywa się tak jak w listach, czy napisach za pomocą indeksu, w kwadratowych nawiasach

print(tup1[:2])                 # Output "(('Python', 1989, 'Java', 1996), (1, 2, 3, 4, 5))"
print(tup2[:2])                 # Output "('Python', 1989)"
print(tup1[2][1])               # Output "b"

print(type(tup2[:2]))           # Output <class 'tuple'>
print(type(tup1[2][1]))         # Output <class 'str'>

# Krotki posiadają mniej metod niż listy, natomiast krotki działają szybciej niż listy

# Tak jak w listach mozemy za pomoca metody len() otrzymac ilość elementow znajdujączch się w krotce
print(len(tup2))                # Output '13'

# Powtórzenie elementów w tuples
# W celu powtórzenia krotki, tak jak listy czy napisu, należy po prostu użyć * operatora
print(tup1[2][:2]*4)            # Output "('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')"

# Przynależność elementów w tuples
# Można wykorzystać operator in, aby sprawdzić, czy krotka zawiera dany element
print('Python' in tuple1)       # Output True

# Krotki mogą zostać w łatwy sposób przekonwertowane na listy, funkcja tuple zamraża listę, a list odmraża krotkę.

###
## Zbiory - SET
## Tworzymy Zbiory
# Zbiór to kolekcja, która jest nieuporządkowana i nieindeksowana. Brak zduplikowanych elementów
# W pojedynczej zmiennej można przechować naraz więcej niż jedną wartość (np. liczbę czy napis).

zbior0 = set()                             # Tworzymy zbiór pusty
zbior1 = set((1, 2, 3, 3, 4, 3, 4, 1, 2))  # Tworzymy zbiór z elementami o typie int 
zbior2 = set(range(10))                    # Tworzymy zbiór z dynamicznie przypisanymi elementami typu int
zbior3 = set('abba')  

print(zbior0, zbior1, zbior2, zbior3)      # Output "set() {1, 2, 3, 4} {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} {'a', 'b'}"

# Konkatenacja elementów w zbiorach
# Połączenie dwóch zbiorow 
print(zbior2.union(zbior1))                # Output "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"

# Dostępne są nastepujace funkcje operujące na elementach zbioru
# Minimum: min()
print(min(zbior1))                 # Output '1'

# Maximum: max()
print(max(zbior2))                 # Output '9'

# Liczba elementów: len()
print(len(zbior1))                 # Output '4'

# Suma wartości wszystkich elementów w zbiorze: sum()
print(sum(zbior2))                 # Output '45'

# Wyznacza część wspólną ze zbiorów
print(zbior2.intersection(zbior1)) # Output "{1, 2, 3, 4}"
print(zbior3.intersection('iwb'))  # Output "{'b'}"

# Wyznacza dopełnienie jednego zbioru nad drugim
print(zbior2.difference(zbior1))   # Output "{0, 5, 6, 7, 8, 9}"

# Tworzymy kopię zbioru
print(zbior2.copy())               # Output "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"

# Możemy rownież spradzić np czy dany elememt jest podzbiorem lub nadzbiorem, jako wynik otrzymujemy Boolean  
print(zbior1.issubset(zbior2))     # Output True
print(zbior2.issuperset(zbior1))   # Output True

# Mozemy przeprowadzic test dla członkostwa elementu w zbiorze
print(2 in zbior1)                 # Output True
print(100 not in zbior1)           # Output True

# Aby posortowac zbiór należy skorzystać z dwóch funkcji built-in: repr() oraz sorted() 
zbior_nsort = set((2.1, 3.7,.6, .1, 1))
print(repr(sorted(zbior_nsort)))   # Output "[0.1, 0.6, 1, 2.1, 3.7]"
