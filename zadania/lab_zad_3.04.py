#!/usr/bin/python3

## 1. Zadanie
# 1.a) Temp
# Napisz python program, który konwertuje temperatury na różne systemy skalowania. 
# Program powinien początkowo oferować wybór z różnymi opcjami.

variant= """
1. Konwersja z Celsjusza na Kelvina
2. konwersja Celsjusza na Fahrenheita”
3. Konwersja Kelvina do Celsjusza”
4. Konwersja Kelvina do Fahrenheita”
5. konwersja Fahrenheita na Celsjusza”
6. konwersja Fahrenheita na Kelvina”
"""
print(variant)

## 1.b) Num 
# Znajdź największą z trzech wprowadzonych liczb i podaj je w kolejosci od największej do najmniejszej.
# W celu wprowadzenia liczb rownież wykorzystaj funkcję pobierania znakow.

## 1.c) Wyznaczanie lat przestępnych 
# Napisz program, który po pobraniu pełnego roku określi, czy dany rok jest rokiem przestępnym.

# --- #

# Tip: Użyj w tym celu funkcji pobierania, wprowadzania manulanie danych do programu. 
# Tip: Python - funkcja input(); 

input_choice = input("Wybierz wariant: ")
print(input_choice)


## 2. Zadanie / filtruj błedny input
# Napisz program, który będzie próbował przechwycić możliwe do przewidzenia błędy, np. 
# - wprowadzenia spacji, zamiast wprowadzenia calego napisu,
# - wcisniecia [Enter],  zamiast wprowadzenia znaku
# - czy wpisania tekstu zamiast liczb, kiedy jest wymagana do wprowadzenia liczba,
# - itp. 
# aby zapobiec tym błędom program wysyła komunikat o błędzie do użytkownika.
# Tip: Użyj w tym celu warunkowych zdań.


## 3. Zadanie / Merge - wykorzystaj 2 w 1
# Rozszerz 1a) 1b) i 1c) o system przechwytywania bledow, ktory zaimplementowaleś w 2. zadaniu.
