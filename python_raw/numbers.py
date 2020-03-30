#!/usr/bin/python3 
# shebang line - wskazuje jaka wersje pythona wybrac domyślne

# Istnieją cztery różne typy liczbowe: zwykłe liczby całkowite, (długie liczby całkowite), liczby zmiennoprzecinkowe i liczby zespolone. 
# Python może być używany rownież jako kalkulator, rozpoznaje cztery podstawowe operatory arytmetyczne: + - * /

## Zwykłe liczby całkowite
a=5
b=10
m=-3

# Odstępy przy operatorach są opcjonalne.
c=a+b*2

print(a,b,c)

# W Pythonie wyrozniamy dodatkowe dwa operatory arytmetyczne: potęgowanie, oraz reszta z dzielenia
print(3**2)   # Output: 9
print(8%3)    # Output: 2

## Długie liczby całkowite
# W pythonie 3 'long integer' nie jest osobnym typem, a Python 2 posiada dwa typy integer'ow - int oraz long. 
print(type(c*c**c))

# W Pythonie liczby całkowite można zapisywać nie tylko w systemie liczbowym dziesiętnym, 
# rownież w dwójkowym (binarnym), ósemkowym (oktalnym) i szesnastkowym (heksadecymalnym).

# konwertujemy liczby na wybrany sytem, korzystjąc z wbudowanych funkcji typu build-in: bin(), oct(), dec(), hex(). 
print(bin(a),oct(b),hex(c))

# Natomiast aby interpreter pythona odczytał Liczby podawane w systemie innym niż dziesietnym 
# należy dopisac na początku liczby zero i litere odpowiadajaca systemowi. 
# Binarnym &ndash; zero i literę b, ósemkowym &ndash; zero i literę o, a w szesnastkowym &ndash; zero i literę x, np.
a_hex=0xf
b_bin=0b10
sum=a_hex + b_bin
print(sum, type(sum))

# Jeżeli wyrażenie zawiera więcej operatorów, są one wykonywane w kolejności znanej z algebry
# W przypadku konieczności zmiany kolejności wykonywania operatorów, używamy nawiasów okrągłych
c_mix=a_hex+b_bin/a*b/c
print(c_mix)

# Zauwazmy, ze zmienna c_mix posiada wartość zmiennoprzecinkową typu float. 
print(type(c_mix))

## Float
# zaznaczmy na poczatek, ze i w tym przypadku znajdzie zastosowanie funkcja castowania w pythonie, znamy ten rodzaj konwersji z napisow
# definujemy zmiennoprzecinkowe wartosci zmiennych
f=float(a)
l=10.2
o=2.
sum=f+l+o

# wydrukujmy informacje o typie danych poszczegolnych zmiennych
print(type(c_mix))
print(type(f),type(l),type(o))
print(sum, type(sum))

# liczby rzeczywiste zapisujemy rowniez w postaci notacji naukowej (mantysa”E”+–wykładnik):
print(1e+6)        # Output: 1000000.0

# Aby odizolować z wyniku dzielenia część ułamkową, użyjemy podwójnego znaku dzielenia:
print(3.0//2.0)    # Output: 1.0

## Liczby zespolone
# w Pythonie zapisywane jako suma części rzeczywistej i części urojonej. 
# Część urojona definiowana jest przez dostawianie na końcu wyrażenia literki "j",
# gdy w wyrażeniu występuje min. jedna liczba urojona, output jest liczbą zespoloną.

print(-2.+2j)      # Output: (-2+2j)
print(-3j/2)       # Output: (-0-1.5j)

# Castowanie wartosci zmiennej do formatu liczb zespolonych
print(complex(a))  
# Output: (5+0j)
type(complex(a))

# W liczbach zespolonych operacje: mod ( % ) oraz floor( // ) są niedostępne.

## Operacje na liczbach
# Python zawiera następujące funkcje, które wykonują obliczenia matematyczne (bez konieczności importowania modułu math)
# Lista wszystkich metod w dokumentacji
# https://docs.python.org/3.8/library/stdtypes.html#numeric-types-int-float-complex

# Dystans miedzy liczba and zero
print(abs(m))

# Wyróżnij max spośród podanych liczb
print(max( a, b, c, m ))

# Wyróżnij min spośród podanych liczb
print(min( a, b, c, m ))

# Zaokrąglij liczbę, round(x [, n] ), gdzie n wskazuje do ilu liczb po przecinku zostanie zokrąglona liczba, 
# jeżeli zostawimy n puste to domyslnie przypisywana jest wartosc n = 0.
print(round(sum))
