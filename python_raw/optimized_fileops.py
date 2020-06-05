#!/usr/bin/python3 
# -*- coding: utf-8 -*-

# Temat: Optymalizacja Programu zorientowanego obiektowo

# by zoptymalizować i poprawić wydajność programu nalezy sprawdzic czy program nie posiada bugow (debugging)
# nalezy dbac o zasoby, warto wykorzystac algorytmy, ktore optymalizuja zlozony proces.
# ja w tym celu uzyje podstawowej biblioteki time i bede mierzyl predkosc wykonywania operacji. 
# zmiercie na poprzedniej wersji
# nastepnie opisujemy  program, zabieramy sie za komentarze, komentarze powinny byc zunikikowane stylem

# Postaram sie Wam pokazac wyrywkowo, przypisac poczatkowe komentraze,
# tlumaczac metody klasy, bede pracowal na poprzednim (niezoptymlaizowanym pliku).


# Class definition
class Pliki:
    
    """ --- Eng --- File operations, object oriented class

    __init__ method
        Funkcja __init__ w języku Python:
        - Służy do definiowania konstruktora parametrycznego
        - Pozwala nadać polom nowo tworzonych obiektów wartości początkowe
        - Pozwala sparametryzować wartości początkowe pól nowo tworzonych obiektów

    Attributes:
        file_name (str): file name.
        phrase (str): Human readable string 
        shift_num (int): number for the encryption or decryption sor secret msg
    Note:

--- PL --- Operacje na plikach, klasa zorientowana obiektowo 
    
    __init__ method

    Attributes:
        file_name (str): file name.
        phrase (str): Human readable string 
        shift_num (int): number for the encryption or decryption ofsome text
    
    Note: 
        - Measuring program performance. 
        - Code optimization 

    Key
    construct 
---"""

    __filename = __file__.split("\\")[-1]

    def __init__(self, file_name = __filename, phrase = '', shift_num = 0):
        """
        :param file_name: string - pelna nazwa pliku.
        :param phrase: string - fraza ."""

        self.file_name = str(file_name)
        self.phrase = str(phrase)
        self.shift_num = int(shift_num)
        #self.otwartych = 0

    def __repr__(self):
        return ""
    
    def get_filename(self):
        """pobieramy nazwe pliku
        Returns: str(file_name) """
        return self.file_name

    def list_dir(self):
        # for scientific purposes
        import os
        arr = os.listdir()
        print(arr) 

    def file_system(self):
        """sprawdzamy czy plik istnieje. Jezeli jest nie jest otwarty, otwieramy go"""
        
        # --------
        # for scientific purposes
        # Sprawdz czas wykonania poszczegolnej funkcji
        # 
        import time
        start = time.time()
        #----------
        
        try: 
            
            # optymalniej jest otworzyc w tym przypadku plik w konstruktorze klasy
            # przypisujac wartosc do zmiennej self.yourvar

            # (Patrz ZAD. DOMOWE) 

            # przyjrzyj sie pierwszej formie zapisu otwierania plikow
            # with open(nazwa_pliku) as f

            # zastosuj druga forme zapisu metkowania w tym przypadku odwolujemy sie do otwierania plikow,   
            # f = open(nazwa_pliku)
            # np. wczytane = self.to_construct()
            # usun global, 
            # zmierz czas


            global f  # globalna zmienna klasowa
            with open(self.file_name) as f:
                print(f'plik o nazwie: "{f.name}" zostal znaleziony i jest', 'zamkniety' if f.closed else 'otwarty')
                #if not f.closed: f.close()
                print(f'plik{f.name} zostal znaleziony i jest', 'zamkniety' if f.closed else 'otwarty')
                
                #-----------------
                end = time.time()
                print(end - start)
                #----------------
                return f

            #return False 
            
        except FileNotFoundError:
            # kod nie może być dalej wykonywany, nazywana jest wyjątkiem (ang. exception)

            print('nie znaleziono pliku')
            end = time.time()
            print(end - start)
            #raise('err')
            return False

    def show_content(self, num=13):
        """ pokaz zawartosc pliku """
        if self.file_system():
            # druga forma przypisywania do zmiennej zapisu otwierania plikow
            wczytane = self.open_file().read(num)            
            print(wczytane)
    
    def open_file(self, mode = "rb"):
        """ Metoda open_file  wskazuje na bazowy plik do odczytu
        Tryby otwarcia pliku to 'rb'
            :return: obj. - otwarty plik"""
        if self.file_system():
            print(f"otwarty plik: {f.name}") 
            ret = open(self.file_name, mode)
            return ret
        else: return False
    
    def close_file(self):
        """zamykamy plik po owczesnej weryfikacji czy jest ta sama nazwa, czy nic sie nie nadpisalo """
        if f.name == self.get_filename:
            f.close()
            print(f"closed {self.file_name}")
        else: return

          
    
    def w_file(self):
        # otwieramy wewnetrznie nowy plik
        
        cop = self.open_file("wb")
        if cop != False:
            cop.write(bytearray('[tekst]', encoding='utf8'))
            self.close_file()
        else: return
     
        
    def copy_file(self):
        """
        funkcja kopiuje plik. 
        Z Nazwy przekazywana jest wartosc przez konstruktora klasy
        """

        try:
            base = self.open_file()                       
            cop = open("kopia " + self.file_name, "wb")   # funkcja open w celu stworzenia kopii do zapisu
            while True:                
                b = base.read(1)                          # wczytujemy z pliku bazowego
                if not b: break      
                cop.write(b)                              # zapis do kopii
            cop.close(); self.close_file()                     # zamykniecie obu plikow           
            print("Kopiowanie zakończone pomyślnie")      # output (jezeli sie udalo)
            return True   
        except FileNotFoundError:
            print('brak')           # output jezeli nie udalo sie znalezc nazwy pliku 
            return False

    def encrypt_msg(self, file_name, shift_num):
        
        """
        funkcja kopiuje plik o nazwie przekazywanej przez paramter funkcji
        :param file_name: pelna nazwa pliku.
        :param shift_num: definiuje przesunięcie 

        napisz funkcje która szyfruje wskazany przez użytkownika plik tekstowy (jezeli istnieje) 
        w oparciu o szyfr Cezara (przesuwanie liter w alfabecie o podaną wartość).     
        """
        pass
      
    def decrypt_msg(self, file_name, shift_num):
        
        """
        funkcja odszyfrowuje plik tekstowy
         :param file_name: pelna nazwa pliku.
         :param shift_num: definiuje przesunięcie 

        napisz funkcje która odszyfruje wskazany przez użytkownika plik tekstowy (jezeli istnieje) 
        w oparciu o szyfr Cezara (przesuwanie liter w alfabecie o podaną wartość).

        gdy programista chce mieć pewność, że dane zostały bezpiecznie zapisane). 
        Służy do tego metoda flush, np. f1.flush()     
        """
        pass


if __name__ == "__main__":


    from time import sleep

    pierwszy_plik = Pliki('kopia test.py')

    #Tworzymy obiekty

    o1 = pierwszy_plik.open_file()
    pierwszy_plik.w_file(); sleep(1)
    pierwszy_plik.close_file(); sleep(1)

    #pierwszy_plik.list_dir()
    
    ol = pierwszy_plik.get_filename()
    print(ol); sleep(1)# BREAKPOINT # Output 
        #<__main__.Pliki object at 0x...>
    l = pierwszy_plik
    print(l); sleep(1)   #wykomentuj metode 
    ##def __repr__(self): return "" 
    ## Output <__main__.Pliki object at 0x...>

    pierwszy_plik.file_system() # BREAKPOINT
    pierwszy_plik.copy_file() # BREAKPOINT
    pierwszy_plik.show_content()   
    
    #print(pierwszy_plik.get_filename())
    
    # mozemy utworzyc nowe obiekty
    obj3kt = Pliki('pop3.py')# BREAKPOINT
    drugi_plik = Pliki('nonsens'); sleep(0.5)
    #wywolujemy metody klasowe
    obj3kt.copy_file(); sleep(0.5)
    obj3kt.show_content(100); sleep(1)

    is_filename_nonsens = drugi_plik.get_filename() # podgladamy nazwepliku
    #print (vars()) # <---- Sledz ale i potem wykomentuj/ usun
    print(is_filename_nonsens) # BREAKPOINT
    drugi_plik.w_file() # BREAKPOINT 
    drugi_plik.show_content() # BREAKPOINT


    # --------------------------- ZAD. DOMOWE -------------------------- #
    # 1. a) Zastosuj breakpointy, aby sledzic przebieg programu - Szukaj znacznikow # BREAKPOINT  
    #    b) Stworz wiecej obiektow, wywolaj je ustaw # BREAKPOINT
    # 2. Dopisz funkcje encrypt_msg oraz decrypt_msg
    # 3. Stworz Klasę Pliki2, ktora otwiera plik w konstruktorze 


# # Class Pliki2format(Pliki) definition:

class Pliki2format(Pliki): 
    """ Stworz Klasę Pliki2, ktora otwiera plik w konstruktorze a w destruktorze go zamyka.
    Zeby bylo latwiej, klasa ta ma dziedziczyc wszystkie atrybuty od klasy Pliki. 
"""   
    pass

    def __str__(self):
        # Wyswietlamy zawrtosc obiektu
        return str(self)

    def create_to_json(self):
        pass
    
    def to_srt(self):
        import pysubs2
        # make_subscript(self, start, stop, stop=20):
        #print('tell()', f.tell())
        pass
     
#EOF
