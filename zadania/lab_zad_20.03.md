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


# II. Zainstaluj środowisko

Dlaczego **nie** będziemy pracować na Pythonie 2 (zobacz sam, URL: https://www.python.org/doc/sunset-python-2/).
Napiszemy pierwszy program wyświetlający napis "Witaj Pythonisto!" 
*Już w tym miejscu możemy zauważyć różnicę między Python 2, a Python 3 - pow. polecenie wygląda inaczej w odniesieniu do werji 2 jak i 3.*


### PRAKTYKA CZYNI MISTRZA

Instalacja narzędzi:

Pobierz ostatnią dostępną wersję dla Windows (https://www.python.org/downloads/)

IDE jest to zintegrowane środowisko pogramistyczne, podczas instalacji Pythona sprawdź proszę czy domyślnie zostało zaznaczone pole wyboru dla oprogramowania IDLE (jeśli nie aktuwuj tą opcję).

Teraz sprawdzimy czy narzędzia programistyczne zostały poprawnie zainstalowane, mamy na to wiele możliwości, przykładowo:
a) uruchom w CMD $ python --version

następnie
b) uruchom program IDLE

Napiszecie teraz pierwszy program w Pythonie. 
Utwórz w tym celu nowy plik, nazwij go: witaj.py.

Python pozwala zarządzać komputerem poprzez wydawanie mu poleceń. 
Pierwszym poleceniem języka Python, które poznasz, jest polecenie wyświetlenia wyniku: *print*

Wpisz polecenie w jezyku Python tak, aby wyswietlił się spersonalizowany komunikat powitalny. 


# III. Zmienne w Pythonie

1. Zmienne zdefiniowane na zewnątrz funkcji są *zmiennymi globalnymi*, to oznacza, że mogą być używane zarówno wewnątrz jak i na zewnątrz funkcji. 
2. Natomiast zmienne zdefiniowane wewnątrz funkcji są *zmiennymi lokalnymi* do użycia tylko wewnątrz funkcji (zmienne lokalne omowione zostaną w dalszej części kursu).

## Otwórz odnośnik do lekcji, w której poznasz możliwości stosowania komentarzy i zmiennych w Pythonie: 

Link: https://github.com/HelloTomek/IwB/blob/master/python_raw/komentarze_i_zmienne.py

Następnie, deklarujemy zmienne globalne: 

1. Zadeklaruj zmienną n, nadaj pustą wartość / Najbardziej ogólny to none, czyli nic.
2. Zadeklaruj zmienną b, nadaj dowolną wartość typu boolean.
3. Zadeklaruj zmienną s, nadaj dowolną wartość typu string.
4. Zadeklaruj zmienną i, nadaj dowolną wartość typu int.
5. Zadeklaruj zmienną f, nadaj dowolną wartość typu float.
6. Zadeklaruj zmienne l oraz m, n:

  6 a) Zastosuj wielokrotne przypisywanie wartości (multiple assignment).
  
  6 b) nadaj im dowolne, lecz różnego typu wartości, może to być przykładowo krotka, lista czy słownik.
 
 
Wyświetl wszystkie wartości korzystając z wcześniej poznanej funkcji print().

Usuń zmeinną s.

---

**W poniższym przykładzie trzy zmienne są przypisane do jednej wartości „2”, czyli przypisane do jednego miejsca w pamięci.** 

*a = b = c = 2*


**Natomiast w przykładzie poniżej, wiele wartości przypisanych jest do wielu zmiennych**

*a, b, c = 1, 2, ”Witaj w Pythonie”*

---

### Podstawowe operacje arytmetyczne
Python rozpoznaje wszystkie cztery podstawowe operatory arytmetyczne: + - * i /

Kolejność wykonywania działań arytmetycznych jest dynamiczna, by ingerować mozemy zastosowac okrągłe nawiasy ().

**Oblicz:** suma = i + f

**Oblicz:** odejmowanie = i - f

**Oblicz:** div = suma / odejmowanie

**Oblicz:** modulo = suma % div

**Oblicz średnią** z dowolnych dwóch zmiennych (wartości liczbowe).

**Oblicz binarnie**: binary = 11011 * 101 

Wypisz wartości *binary* w systemie dziesiętnym, oraz dwójkowym

**Wyświetl również wartości: dla sredniej, sumy, div i modulo.**

# Zastanów się:

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


# II. Zainstaluj środowisko

Dlaczego **nie** będziemy pracować na Pythonie 2 (zobacz sam, URL: https://www.python.org/doc/sunset-python-2/).
Napiszemy pierwszy program wyświetlający napis "Witaj Pythonisto!" 
*Już w tym miejscu możemy zauważyć różnicę między Python 2, a Python 3 - pow. polecenie wygląda inaczej w odniesieniu do werji 2 jak i 3.*


### PRAKTYKA CZYNI MISTRZA

Instalacja narzędzi:

Pobierz ostatnią dostępną wersję dla Windows (https://www.python.org/downloads/)

IDE jest to zintegrowane środowisko pogramistyczne, podczas instalacji Pythona sprawdź proszę czy domyślnie zostało zaznaczone pole wyboru dla oprogramowania IDLE (jeśli nie aktuwuj tą opcję).

Teraz sprawdzimy czy narzędzia programistyczne zostały poprawnie zainstalowane, mamy na to wiele możliwości, przykładowo:
a) uruchom w CMD $ python --version

następnie
b) uruchom program IDLE

Napiszecie teraz pierwszy program w Pythonie. 
Utwórz w tym celu nowy plik, nazwij go: witaj.py.

Python pozwala zarządzać komputerem poprzez wydawanie mu poleceń. 
Pierwszym poleceniem języka Python, które poznasz, jest polecenie wyświetlenia wyniku: *print*

Wpisz polecenie w jezyku Python tak, aby wyswietlił się spersonalizowany komunikat powitalny. 


# III. Zmienne w Pythonie

1. Zmienne zdefiniowane na zewnątrz funkcji są *zmiennymi globalnymi*, to oznacza, że mogą być używane zarówno wewnątrz jak i na zewnątrz funkcji. 
2. Natomiast zmienne zdefiniowane wewnątrz funkcji są *zmiennymi lokalnymi* do użycia tylko wewnątrz funkcji (zmienne lokalne omowione zostaną w dalszej części kursu).

## Otwórz odnośnik do lekcji, w której poznasz możliwości stosowania komentarzy i zmiennych w Pythonie: 

Link: https://github.com/HelloTomek/IwB/blob/master/python_raw/komentarze_i_zmienne.py

Następnie, deklarujemy zmienne globalne: 

1. Zadeklaruj zmienną n, nadaj pustą wartość / Najbardziej ogólny to none, czyli nic.
2. Zadeklaruj zmienną b, nadaj dowolną wartość typu boolean.
3. Zadeklaruj zmienną s, nadaj dowolną wartość typu string.
4. Zadeklaruj zmienną i, nadaj dowolną wartość typu int.
5. Zadeklaruj zmienną f, nadaj dowolną wartość typu float.
6. Zadeklaruj zmienne l oraz m, n:

  6 a) Zastosuj wielokrotne przypisywanie wartości (multiple assignment).
  
  6 b) nadaj im dowolne, lecz różnego typu wartości, może to być przykładowo krotka, lista czy słownik.
 
 
Wyświetl wszystkie wartości korzystając z wcześniej poznanej funkcji print().

Usuń zmeinną s.

---

**W poniższym przykładzie trzy zmienne są przypisane do jednej wartości „2”, czyli przypisane do jednego miejsca w pamięci.** 

*a = b = c = 2*


**Natomiast w przykładzie poniżej, wiele wartości przypisanych jest do wielu zmiennych**

*a, b, c = 1, 2 ”,Witaj w Pythonie”*

---

### Podstawowe operacje arytmetyczne
Python rozpoznaje wszystkie cztery podstawowe operatory arytmetyczne: + - * i /

Kolejność wykonywania działań arytmetycznych jest dynamiczna, by ingerować mozemy zastosowac okrągłe nawiasy ().

Oblicz: suma = i + f

Oblicz: odejmowanie = i - f

Oblicz: div = suma / odejmowanie

Oblicz: modulo = suma % div


**Oblicz w systemie binarnym**: binary = 11011 * 101 

**Wypisz wartości *binary* w systemie dziesiętnym, oraz dwójkowym.**

**Wyświetl rownież wartości: suma, div i modulo.**

# Zastanów się

a = 1

b = 2,3

suma_blad = 1 + 2,3

print(suma_blad) # Zwróć uwagę na rezultat.


suma_blad = a + b

print(suma_blad) # dlaczego otrzymaliśmy błąd, jak naprawić program? 



**Przeanalizuj program, a następrnie wyświetl typ danych wszystkich dotąd stosowanych zmiennych.**

- Zatanów się jak pojedynczym poleceniem Pythona i bez użycia nawiasów, przemnożyć zmienną *a* przez *a+2*

