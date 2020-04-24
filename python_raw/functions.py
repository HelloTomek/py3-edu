##!/usr/bin/python3

## Funkcje w Pythonie

# Funkcja w programowaniu - zdefiniowana sekcja wykonująca określony blok kodu. Funkcje, procedury i metody 
# są wygodnym sposobem dzielenia kodu na bardziej czytelne bloki, pozwalając tym samym ustrukturyzować program. 
# Wbudowane funkcje typu build-in: https://docs.python.org/3/library/functions.html

## Tworzymy pustą funkcję

"""
PEP 257 -- Docstring Conventions
Pod każdą funkcją znajdziesz krótką adnotacje - docstring - opis funkcji dla developera.  
Docstringi w Pythonie tworzy się zaraz pod nagłówkiem - w ciele funkcji, procedury czy metody. 

"""

# Funkcje są definiowane poprzez użycie słowa kluczowego def, nazwę funkcji, nawiasy oraz na końcu nagłówka znajduje się dwukropek. 
# PEP 8 (styl i konwencja) - zapisujemy nazwy małymi literami oddzielamy je podkreslnikiem
# Jeżeli funkcja nie wymaga informacji z zewnątrz nawiasy pozostawiamy puste.

def empty_function():    # podstawowy zapis, tzw. baza
    """Pusta funkcja"""
    # stosujemy wcięćia, tak samo jak robilismy m.in. podczas pisania instrukcji warunkowych if ..., else ...
    # W Pythonie do pisania pustych funkcji używamy instrukcji pass. 
    # pass jest specjalną instrukcją w Pythonie, która nie robi po prostu nic (dummy statement).
    pass   # Puste funkcje - placeholdery, definiujemy w początkowym procesie konstruowania szkieletu programu.
  
## Tworzymy funkcję wyznaczającą rok przestepny 
# we wnetrzu każdej niepustej funkcji moze znajdowac sie dowolna ilość poleceń

def leap_yr():
    """Funkcja sprawdza czy rok jest rokiem przestepnym lub nie"""
    while True:
        try: 
            year = int(input("Podaj rok: "))
        except ValueError: 
            print("nie wpisales poprawnie roku")
        else: 
            print(f'rok {year}',['nie jest rokiem przestępnym','jest rokiem przestępnym'][year%400 == 0 or (year%4 == 0 and year%100 != 0)])
        finally:
            keyin = input("\nChcesz wpisac nastepny rok? t/n> ")
            if keyin.lower() in ['n','nie']: break 
            else: continue

# Teraz gdy potrfimy juz stworzyć funkcje należy je odpowiednio wywołac, zatem wystartujemy program, 
# wywoływując najpierw nasza pusta funkcję, jak sie domyslamy nie otryzmamy żadnego komunikatu. 
empty_function()

# Wywoływujemy funkcję wyznaczającą rok przestepny
leap_yr()

# Funkcje to sekcje kodu, które są odizolowane od reszty programu i wykonywane tylko po ich wywołaniu. 
# Funkcje mogą być wywoływana wielokrotnie, za każdym razem mogą przyjmować inne parametry, 
# aby móc przekazać parametr do funkcji należy go zdefiniować już w naglówku.
# W pierwszych przykładach - zostawialiśmy nawias pusty, natomiast aby zmienić sposób działania 
# musimy przekazać wartości do funkcji podczas jej wywolywania.

def welcome(n='tomek'):  # paramter n - gdy wywolamy funkcje bez argumentu, jako domyślny parametr figuruje 'tomek'
    """Powitanie - funkcja modyfikuje napis"""
    print(f"hello {n}".title())    #  wyprintujmy sobie znany nam z poprzednich czesci napis  

# Ważna cehcą funkcji, metod i procedur jest fakt, że aby wykonać zawarte w nich instrukcje,  
# możemy wywołać blok kodu z dowolnego miejsca w programie, oczywiscie po uprzednim wczytaniu funkcji.

## Istnieją dwa sposoby przekazywania parametru do funkcji :
# - przekazywanie przez wartość

welcome('ewa')
welcome('wojtek')
welcome()

## Tworzymy funkcje z nieokreslona liczba argumentow
def function_with_args(*nums): # *args 
    """Funkcja sumuje wszytskie dowolne wartosci liczbowe"""
    total = 0
    for i in nums:
        total += i
        #return total
    return total
    
print(function_with_args(12,31,56,14))
    
## Tworzymy 3 slowniki z danymi użytkowników
user1 = {'nick': 'ewa', 'pesel': '88071901123'}
user2 = {'nick': 'wojtek', 'pesel': '88071901124'}
user3 = {'nick': 'tomek', 'pesel': '88071901125'}

## Tworzymy funkcje z nieokresloną liczbą argumentów
def function_with_kwargs(**kwargs):
    """Funkcja wypisuje wszystkie elementy - keyword args"""
    print(kwargs)

function_with_kwargs(nick=welcome(), pesel='88071901122')   # nick : brak return -> none

function_with_kwargs(nick=user1['nick'], pesel=user1.get('pesel')) 
function_with_kwargs(nick=user2['nick'], pesel=user2.get('pesel')) 
function_with_kwargs(nick=user3['nick'], pesel=user3.get('pesel')) 


## Dla zobrazowania przekazwania danych referencjnych, tworzymy pustą listę, 
# jest to drugi sposób przekzywania danych w Pythonie
# - Przekazywanie danych przez referencję

l1=[]
def by_reference():
    """Przekazywanie danych przez referencję"""
    l1.append(user1.get('nick'))
    l1.append(user2.get('nick'))
    l1.append(user3.get('nick'))

print(f'Przed przekazaniem danych przez referencję l1 wyglądało tak : {l1}')
by_reference()
print(f'po przekazaniu danych przez referencję l1 wygląda teraz tak : {l1}')

## Zwracanie wartości funkcji - za pomocą wyrażenia return
# W Pythonie funkcja może zwracać tyle wartości ile jest potrzebne, brak ograniczeń
# "Function returns a value, while procedure doesn’t"

def grade_conv(grade) -> (str):
    """
    funkcja wypisuje slownie oceny
    zwracana jest wartosc typu String
    """
    if grade>=90:
        return "bdb"
    elif grade>=75:
        return "db"
    elif grade>=60:
        return "dst"
    elif grade>=50:
        return "dop"
    else:
        return "ndst"

# Wywolujemy trzykrotnie tę samą funkcję z róznymi argumentami, wartości "metkujemy" 
ewa = grade_conv(80)
wojtek = grade_conv(91)
tomek = grade_conv(51)

print('ocena ewa:', ewa, '\nocena wojtek:', wojtek, '\nocena tomek:', tomek )

## Tworzymy przykład dla funkcji z rekurencją 
# Funkcje rekurencyjne to funkcje, które wywołują same siebie bezpośrednio lub za pośrednictwem innych funkcji.

def iter_factorial(n):
    """Obliczanie silni iteracyjnie, pierwszy sposób"""
    tmp=1 # zmienna pomocnicza
    if n in (0,1):  # dla n = 0 lub 1 zwróć 1
        return 1
    else:
        for i in range(2, n+1):  # n>1 mnożymy przez kolejne liczby od 2 do n
            tmp = tmp*i
    return tmp

def rec_factorial(n):
    """Obliczanie silni rekurencyjnie, drugi sposób"""
    if n < 2:
        return 1
    return n * rec_factorial(n - 1)

fi1,fi2,fi3,fi4,fi5 = iter_factorial(1), iter_factorial(2), iter_factorial(3), iter_factorial(4), iter_factorial(5)
f1,f2,f3,f4,f5 = rec_factorial(1), rec_factorial(2), rec_factorial(3), rec_factorial(4), rec_factorial(5)

print('\n1! =', f1, ' \t  2! =', f2, ' \t  3! =', f3, ' \t  4! =', f4, ' \t  5! =', f5) 
print('1! =', fi1, ' \t  2! =', fi2, ' \t  3! =', fi3, ' \t  4! =', fi4, ' \t  5! =', fi5,'\n') 

print(function_with_args(f1,f2,f3,f4,f5))

# Funkcja jest bardziej ogólnym terminem, a wszystkie metody są również funkcjami

# Zmienne globalne i lokalne 
# W Pythonie zmienne zdefiniowane na zewnątrz funkcji są zmiennymi globalnymi, 
# to oznacza, że mogą być używane zarówno wewnątrz jak i na zewnątrz funkcji. 
# Natomiast zmienne zdefiniowane wewnątrz funkcji są zmiennymi lokalnymi do użycia tylko wewnątrz funkcji.

pi = 3.14

def area_of_circle(radius):
    """Funkcja oblicza pole koła"""
    area = pi * radius * radius
    print('Pole: ' + str(area))

# Jeśli chcielibyśmy w powyższym przykładzie wartość zmiennej globalnej, nadpisać wartością zmiennej lokalnej 
# umieszczonej wewnątrz funkcji o tej samej nazwie, to musimy do zmiennej „pi” dopisać słowo „global”
 
def update_pi(newPi):
    """Funkcja aktualizuje wartosc pi"""
    global pi
    pi = newPi

# Pole koła przy pi (dwa miejsca po przecinku)
area_of_circle(500)

# Funkcja aktualizuje wartosc pi
update_pi(3.14159265)

# Pole koła przy pi (dziesięć miejsc po przecinku)
area_of_circle(500)
