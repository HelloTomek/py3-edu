# I. Wybierz i opisz jeden z obszarów zastosowania Pythona, podaj przykłady:

1. Programowanie systemowe
2. GUI
3. Analiza danych
4. Nauka programowania
5. Programowania webowe
6. Programowanie bazodanowe
7. Prototyping
8. Automatyzacja
9. Python w grach i integracja

# II. Zainstaluj lokalnie środowisko
Napiszemy pierwszy program wyświetlający napis "Hello Tomek!"

Instalacja narzędzi
Python 2 (https://www.python.org/doc/sunset-python-2/)

Pobierz ostatnią wersję dla Windows (https://www.python.org/downloads/)

IDE / zintegrowane środowisko pogramistyczne (podczas instalacji pythona sprawdz czy jest zaznaczony checkbox dla oprogramowania IDLE )

Sprawdź czy narzędzia programistyczne zostały poprawnie zainstalowane

a) uruchom w CMD $ python --version

b) uruchom IDLE

Pierwszy python program
Python pozwala zarządzać komputerem poprzez wydawanie mu poleceń. Pierwszym poleceniem języka Python, które poznasz, jest polecenie wyświetlenia wyniku: print

output "Hello Tomek!"

# III. Zmienne python

1. Zmienne zdefiniowane na zewnątrz funkcji są *zmiennymi globalnymi*, to oznacza, że mogą być używane zarówno wewnątrz jak i na zewnątrz funkcji. 
2. Natomiast zmienne zdefiniowane wewnątrz funkcji są *zmiennymi lokalnymi* do użycia tylko wewnątrz funkcji.

## Otwórz odnośnik do maski stosowania komentarzy w Pythonie: 

(https://github.com/HelloTomek/IwB/blob/master/python_raw/komentarze_i_zmienne.py)

Nastepnie, deklarujemy zmienne globalne: 

zadeklaruj zmienną n, nadaj pustą wartość / Najbardziej ogólny to none, czyli nic.
zadeklaruj zmienną b, nadaj wartość typu boolean.
zadeklaruj zmienną s, nadaj wartość typu string.
zadeklaruj zmienną i, nadaj wartość typu int.
zadeklaruj zmienną f, nadaj wartość typu float.
zadeklaruj zmienną l , nadaj wartość typu lista lub (tupla), czy {słownik}.
Zastosuj wielokrotne przypisywanie wartości (multiple assignment).

Wyświetl wszystkie wartości korzystając z wcześniej poznanej funkcji print().

Wyswietl typ danych dowolnej zmiennej.

**w poniższym przykładzie trzy zmienne są przypisane do jednej wartości „2”, czyli przypisane do jednego miejsca w pamięci
a = b = c = 2**
 
**w poniższym przykładzie wiele wartości przypisanych jest do wielu zmiennych
a, b, c = 1, 2 ”,Witaj w Pythonie”**

### Podstawowe operacje arytmetyczne
Python rozpoznaje wszystkie cztery podstawowe operatory arytmetyczne: + - * i /

Kolejność wykonywania działań arytmetycznych jest dynamiczna, by ingerować mozemy zastosowac okrągłe nawiasy ().

Oblicz: sum = i + f

wypisz wartość sum.
