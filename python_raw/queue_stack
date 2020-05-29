#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------- #
# Liniowe struktury danych   #
# -------------------------- #

## Kolejka w Pythonie (ang. queue)  
# Nowy element dodawany jest na końcu, analogicznie do klienta, który zawsze staje na końcu kolejki. 
# Usunięcie z kolejki odpowiada obsłużeniu klienta w sklepie, czyli osoby, która aktualnie czekała najdłużej.

class Kolejka:
    
    """Bufor typu FIFO - pierwszy na wejściu, pierwszy na wyjściu
    Operacje: zakolejkuj, odkolejkuj, mozemy tez spojrzec czy kolejka jest pusta
    ile liczy elementow, oraz jaki element stoi na poczatku kolejki """

    def __init__(self, elementy = None): # Kostruktor
        if elementy is None:
            elementy = []
        self.__kolejka = elementy

    def __str__(self):
        return str(self.__kolejka)

    def czy_pusta(self):
        """czy kolejka jest pusta"""
        return len(self.__kolejka) == 0

    def zakolejkuj(self, element):   
        """enqueue - nowe dane dopisywane są na końcu kolejki"""
        self.__kolejka.append(element) 

    def odkolejkuj(self):            
        """usuwany jest element, ktory znajduje się z przodu kolejki"""
        return self.__kolejka.pop(0)

    def pierwszy(self):             
        """jaki jest pierwszy element"""
        return self.__kolejka[0]
    
    def size(self):         
        """Ilość elementów w kolejce"""
        return len(self.__kolejka)

## Stos w Pythonie (ang. Stack) - dane dokładane są na wierzch stosu i z wierzchołka stosu są pobierane 
# Ideę stosu danych można zilustrować jako stos położonych jedna na drugiej książek – 
# nowy egzemplarz kładzie się na wierzch stosu i z wierzchu stosu zdejmuje się kolejne egzemplarze. 
# Elementy stosu poniżej wierzchołka można wyłącznie obejrzeć, aby je ściągnąć, 
# trzeba najpierw po kolei ściągnąć to, co jest nad nimi.

class Stos:

    """ bufor typu LIFO - ostatni na wejściu, pierwszy na wyjściu
    Operacje: push, pop, mozemy tez spojrzec czy stos jest pusta
    ile liczy elementow, oraz jaki element stoi na koncu stosu """

    def __init__ (self, elementy = None): # Kostruktor
        if elementy is None:
            elementy = []
        self.__stos = elementy
 
    def push(self, s):      
        """Dodawanie elementu"""
        self.__stos.append(s)   
    
    def pop(self):          
        """Usuwanie elementu"""
        self.__stos.pop(len(self.__stos)-1)
    
    def size(self):         
        """Ilość elementów na stosie"""
        return len(self.__stos)
    
    def top(self):          
        """Zwraca ostatni element"""
        return self.__stos[ len(self.__stos)-1 ]
    
    def empty(self):        
        """Sprawdza czy stos jest pusty"""
        if len(self.__stos) == 0 : return True
        else : return False


if __name__ == '__main__':
    
    print("\nPrzykładowe działania na kolejce: ")
 
    k = Kolejka()
    k.zakolejkuj('Informatyka'); print(k)
    k.zakolejkuj('w'); print(k)
    k.zakolejkuj('Biznesie'); print(k)
    k.zakolejkuj('2020'); print(k)
    
    d = k.size()
    print ('Ilosc elementow w kolejce :', d)   
    print()
    print(k.pierwszy())
    k.odkolejkuj()
    print(k.pierwszy())
    k.odkolejkuj()
    print(k)
    print ('Ilosc elementow w kolejce :', d)   

    print('\n',"---"*10)
    
    print("\nPrzykładowe działania  na stosie:")
    
    stos = Stos()
    for i in range(0, 10) : 
        stos.push(i)
    
    l = stos.size()
    print ('Ilosc elementow na stosie :', l)
    print ('Obiekty na stosie :')
    for i in range(l) :
        print(stos.top())
        stos.pop()
