#!/usr/bin/python3

## Tworzymy listy
# Lista to kolekcja, która jest uporządkowana i zmienna. Umożliwia duplikaty elementów.
# Link do dokumentacji https://docs.python.org/3.8/library/stdtypes.html#lists
# Listy tworzymy używając nawiasów kwadratowych, rozdzielając ich poszczególne elementy przecinkami
# Lista posiada przypisane indeksy, zaczynające się od zera. Jeżeli chcemy je wywoałc, 
# należy podać nazwę zmiennej i numer indeksu w kwadratowym nawiasie [0,1,2,3,4,5,6,...,-6,-5,-3,-3,-2,-1].

lista1 = []               # Utworzona została pusta lista
lista2 = list('0')        # Utworzona została lista z jednym elementem '0' - list() constructor
lista3 = [3, 2, 1]        # Utworzona została nowa lista z elementami [3,2,1]
lista4 = list(range(10))  # Utworzona została dynamicznia lista z indeksem jak i wartosciami od 0 do 9

print(lista2,lista1)      # Output "['0'] [] "
print(lista3, lista3[0])  # Output "[3, 1, 2] 3"
print(lista4)             # Output "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

# Konkatenacja list
# podobnie jak z napisami laczenie list odbywa sie na kilka sposobow
# np. znany nam sposob poprzez uzycie + operatora 
lista5 = lista3 + lista4 
print(lista5)             # Output "[3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

## Python List/Array Methods
# Listy mogą składać się z elementów o zróżnicowanym typie danych

# Dodawanie elementów na koniec listy
lista3.append(0)   
print(lista3)            # Output "[3, 2, 1, 0]"

lista1.append('tomek')
lista1.append(1.)
lista1.append([()])
print(lista1)            # Output "['tomek', 1.0, [()]]"

# Konkatenacja list - metoda extend()
lista6=[10,11,12]
lista3.extend(lista6)
print(lista3)            # Output "[3, 2, 1, 0, 10, 11, 12]"

# Skorzystajmy z petli for, ktora "przeloopuje" wszystkie elementy z jednej listy i dołączy je do drugiej
for x in lista3:
  lista6.append(x)
print(lista6)            # Output "[10, 11, 12, 3, 2, 1, 0, 10, 11, 12]"

# Usuwanie elementu na określonej pozycji, o indeksie
lista3.pop(2)      
print(lista3)            # Output "[3, 2, 0, 10, 11, 12]"

# Czyszczenie całej listy
lista1.clear()
print(lista1)            # Output "[]" 

# Tworzenie wycinków. 
# Notacja do krojenia list (slicing) w Pythonie powinna byc nam znana, zapis analogicznie do napisow
# Nalezy podać początek i koniec (liczonych od 0 i rozdzielonych dwukropkiem) w nawiasach kwadratowych po nazwie listy. 
# Można także podać (po drugim dwukropku), co który element ma zostać wybrany, domyslnie step = 1.

print(lista6[3:5])      # Output "[3, 2]" 
print(lista6[:2])       # Output "[10, 11]" 
print(lista6[:-1])      # Output "[10, 11, 12, 3, 2, 1, 0, 10, 11]"
print(lista6[::-1])     # Output "[12, 11, 10, 0, 1, 2, 3, 12, 11, 10]"     

# Sortowanie elementów w liście (w odwrotnej kolejności)
# Kopiowanie listy
lista3.sort(reverse=True)
lista7 = lista3.copy()
print(lista3, lista7)

# Output typ int - zliczamy powtarzające się elementy w liscie 
# Metoda count() służy do zliczenia, ile razy element występuje w liście.
print(lista7.count(3))	# Output 1

# Output typ int - otrzymujemy pozycję (indeks) pierwszego elementu, który pojawił się w liście
print(lista7.index(3))	# Output 3

# Wstaw w wyznaczonej pozycji element
pozycja = 5
element = 10
lista7.insert(pozycja,element)	
print(lista7)     # Output "[12, 11, 10, 3, 2, 10, 0]"

# Usuwanie pierwszego napotkanego elementu o danej wartości
lista5.remove(6)
print(lista5)     # Output "[3, 2, 1, 0, 1, 2, 3, 4, 5, 7, 8, 9]"

# Na koniec posortujemy elementy z listy
lista5.sort()
print(lista5)     # Output "[0, 1, 1, 2, 2, 3, 3, 4, 5, 7, 8, 9]"
