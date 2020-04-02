#!/usr/bin/python3

## DICT - dictionary
## Tworzymy słowniki
# Link do dokumentacji https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# Słowniki w Pythonie to złożone typy danych *standard mapping type*, nieuporządkowane lecz zmienne. 
# Przypominaja poznane wczesniej listy, jednak różnią się m. in. tym, że dostęp do wartości uzyskujemy za pomocą klucza. 
# Inne typy danych mają przypisną wartość jako element, słownik ma parę: klucz i wartość.

# Definiujemy słowniki
d1 = {'raz': 1, 'dwa': 2, 'trzy': 3}
d2 = dict({'trzy': 3, 'raz': 1, 'dwa': 2})
d3 = dict(raz=1, dwa=2, trzy=3)
d4 = dict([('dwa', 2), ('raz', 1), ('trzy', 3)])
d5 = dict(zip(['raz', 'dwa', 'trzy'], [1, 2, 3]))
djoin = dict(a=d1, b=d2, c=d3, d=d3, e=d5)

print("wszystkie słowniki są jednakowe\n", djoin if(d1 == d2 == d3 == d4 == d5) else \
"nie wszystkie słowniki są jednakowe")

dict0 = {}               # Pusty słownik
dict1 = dict()           # Pusty słownik
    
print(dict0 == dict1)    # True

# Klucz wskazuje na wartosc
dict2 = {1:'160', 2:'161', 3:'B'}
dict3 = {3:'160B', 4:'161B'}

# Wyświetlanie wszystkich > 
# - elementow
print(dict2.items())     # Output dict_items([(1, '160'), (2, '161'), (3, 'B')])

# - nazw wartości
print(dict2.values())    # Output dict_values(['160', '161', 'B'])

# - nazw kluczy
print(dict2.keys())      # Output dict_keys([1, 2, 3])

# Wyswietlanie wartości jest przypisane do nazwy klucza, używamy w tym celu > 
# - funkcji get() 
print(dict2.get(1))      # Output '160'

# - lub zaraz po nazwie zmiennej wpisujemy w kwadratowych nawiasch nazwę klucza
print(dict2[1])          # Output '160'

# Konwersja kluczy słownika do listy
print(list(dict2))       # Output [1, 2, 3]

# Tricki na słownikach
print(dict2, dict3)      # Output {1: '160', 2: '161', 3: 'B'} {3: '160B', 4: '161B'}
print({*dict2,*dict3})   # Output {1, 2, 3, 4}
print({**dict2,**dict3}) # Output {1: '160', 2: '161', 3: '160B', 4: '161B'}

# Sprawdź czy klucz jest / lub go nie ma w słowniku 'in' / 'not in'
print('1 jest kluczem w dict2' if 1 in dict2 else False) # Output '1 jest kluczem w dict2'
print('B' not in dict2)  # True

# Metoda get(), może nam również pomóc zweryfikować czy dana nazwa klucza w słowniku istnieje. 
# W tym celu zastosujemy > dict.get(key[, value]) 
print(dict2.get(123,'nie ma takiego klucza w słowniku')) # Output 'nie ma takiego klucza w słowniku'

# Dodaj element
dict3[5] = 'IwB'  
print(dict3)             # Output {3: '160B', 4: '161B', 5: 'IwB'}

# Usuń element
print(dict2.pop(3))      # Output 'B'
print(dict2.popitem())   # Output (2: '161')
del dict2[1]             # Deleted (1: '160')
print(dict2)             # Output {}

# możemy usunąć całą zawartość słownika jedną funkcja >>> clear(). 
# W celu weryfikacji zmierzmy dlugość słownika, oraz wyswietlimy jego zawartość
print(dict3, len(dict3)) # Output {3: '160B', 4: '161B', 5: 'IwB'} 3 
dict3.clear()
print(dict3, len(dict3)) # Output '{} 0'

# Dodatkowo wykorzystując pętle możemy utworzyc dynamiczny słownik
dict4 = {x: x**2 for x in range(1,10,2)}
print(dict4)             # Output {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

## Switch
## Tworzymy przełącznik - instrukcja wyboru
# Notacja wykorzystująca słowniki używana jest m.in. w funkcji wyboru, jaką jest switch().
# Sekwencja if(), elif(), elif(), ... zastępuje instrukcje switch. 
# Stosowanie przełącznika jest przydatną konstrukcją programistyczną, 
# która nie tylko zapewnia lepszą wydajność niż instrukcja if-else, ale także zapewnia łatwiejszy do zarządzania kod.

month_switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
print(month_switcher[4]) # Output April 
