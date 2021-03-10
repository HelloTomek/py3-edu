# Ciągi znaków w Pythonie otoczone są pojedynczymi lub podwójnymi cudzysłowami. 
# String jest to typ sekwencyjny - w jednej zmiennej możemy przechować wiele wartości.
# Dane typu String w Pythonie są niemutowalne (niezmienne).
# Spójrzmy zatem bliżej na formatowanie ciągów i niektóre metody stosowane na danych typu String. 
# Notacja: (''), (""), (''' '''), (""" """").
                                           
hello = 'hello'    
world = "world"              
hw = """
Hello World
"""

print(world)       

# Konkatencja - w programowaniu oznacza łączenie dwóch wyrażeń.
hello_world = hello + ' ' + world

# Argumenty pozycyjne, padding 
print("{h}{w}".format(h=hello, w=world))
print('{:>10}'.format(hello))
print('{:^10}'.format(world))

# F-Strings (w Python pow. 3.6)
print(hello_world)
print(f'{hello}\n{world}')

## Formatowanie ciągów znaków
# Zmieniamy format (castowanie), aby wymusic format danych typu String, mozemy skorzystac z wbudowanej funkcji str().
# str() - tworzy string ze zroznicowanego typu danych, tj. strings, integer literals oraz float literals.

# W ponizszym przypadku z liczby na tekst 

print(type(str(1)))

# Print zakończony jest „niewidzialnym” znakiem nowej linii (\n), mozemy sie od tego uwolnić

print(hello, end='')
print(world)

## Metody ciągów znaków
## Lista wszystkich metod w dokumentacji
# https://docs.python.org/3.8/library/stdtypes.html#string-methods

# Python zapewnia zwięzłą składnię dla danych typu String. 

# Przykładowo do tworzenia podlisty z napisu (sublist), 
# aby uzyskać dostęp do podzbiorów ciagów znakow, możemy skorzystać z metody znanej jako 
# Python string slicing, wg. zasady: s[:i] + s[i:] == s, dla dla kazdego index'u i 

# String slicing - ciecie napisow.

print(hello_world[4:-4])

print(hw[1:6])          # tniemy napis od index'u 1 do 6 (exclusive) 
print(hw[3:])           # tniemy napis od index'u 3 do konca
print(hw[:3])           # tniemy od poczatku napisu do index'u 3 (exclusive)
print(hello[:-1])       # ciecie negatywne, liczone od konca - index 
print(hello[::-1])      # ciecie odwrotne, step -1
print(hello[:])         # zwraca nam caly napis w niezmienionej formie

# Prawostronnie wyjustowany napis, padding spacjami
print(hello.rjust(10))

# Centrujemy napis, padding spacjami
print(world.center(10))     

# Zamienia znak/znaki
print(hw.replace('Hello', 'Bye'))

# Wszystkie jako uppercase 
print(hello.upper())

# Wszystkie jako lowercase 
print(world.lower())

# Napis jako tytuł
print(hw.title())

# Zmienia pierwszą literę w ciągu na dużą
print(hw.capitalize())

# Odwraca rodzaj każdej litery – małe na duże, duże na małe
print(hello_world.swapcase())

# Output typ int - zmierz dlugość napisu
print(len(hello))

# Output typ int - zlicz ile razy wystepuje nasz substring w napisie
sub = 'e'
print(hello.count(sub))

# Rozszczepiamy napis do listy
print(hw.split(' '))

# Znajdz pozycje
print(hello.find('e'))

# Output typ boolean - poczatek sekwencji znakow
print(hw.startswith('Hello'))

# Output typ boolean - koniec sekwencji znakow
print(world.endswith('d'))

# Output typ boolean  - Wszystkie jako alphanumeric
print(world.isalnum())

# Output typ boolean - Wszystkie jako alphabetic
print(hello.isalpha())

# Output typ boolean - Wszystkie jako numeric
print(hw.isnumeric())         # False

## Znaki specjalne notacja backslesh'owa oraz hex, wyjasnienie: 
# \a	  0x07	Alert
# \b	  0x08	Backspace
# \cx	 	Control-x
# \C-x	 	Control-x
# \e	  0x1b	Escape
# \f	  0x0c	Formfeed
# \M-\C-x	 Meta-Control-x
# \n	  0x0a	Nowa linia
# \nnn	  Osemkowa Notacja, gdzie n is in the range 0.7
# \r	  0x0d	return
# \s	  0x20	Spacja
# \t	  0x09	Tab
# \v	  0x0b	Vertical tab
# \x	  Character x
