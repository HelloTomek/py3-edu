#!/usr/bin/python3

## Tworzymy zmienne o wartosciach logicznych 
# Python posiada specjalny typ danych logicznych, istnieją dwie wartości logiczne: True i False, stos. (1 i 0). 
# Wartości Boolean służą do przechowywania prawdziwych i fałszywych wartości. Typ danych został nazwany na cześć bryt. matematyka Boole'a.
# Notacja: wielkie litery są ważne, ponieważ 'true' i 'false' nie są wartościami logicznymi w Pythonie.

x,y = 1, 0               # deklarujemy wartości zmiennych
a,b = True, False
c,d = bool(x), bool(y)

print(a,b,c,d)           # Output "True False True False "

# Wartości logiczne True albo False są najczęściej zwracane, kiedy porównujemy ze sobą dwie wartości
e,f = x == x, x != x
g,h = x >= y, x < y 

print(e,f,g,h)           # Output "True False True False"

# Operatory logiczne
# Możemy zaprzeczyć zawartość używając not (negacja) - zmieniamy jego wartość na przeciwną

print(not b)             # Output True
print((not a) == (b))    # Output True

# Operatory logiczne 'and', 'or' oraz 'xor' pozwalają na budowanie kompletnych zdań logicznych
# AND
print()
print(a and a, end=' \t ')
print(a and b, end=' \t ')
print(b and a, end=' \t ')
print(b and b)

# OR
print(a or a, end=' \t ')
print(a or b, end=' \t ')
print(b or a, end=' \t ')
print(b or b)

# XOR  - symbol '^' w Pythonie traktowany jest jako bitwise operator (Integer)
print(a ^ a, end=' \t ')
print(a ^ b, end=' \t ')
print(b ^ a, end=' \t ')
print(b ^ b,'\n')

# Sprawdzimy czy podane wyrażenia są tautologią
print(((a and not a) or (not a and a)) == a ^ a, end=' | ')
print(((a and not b) or (not a and b)) == a ^ b, end=' | ')
print(((b and not a) or (not b and a)) == b ^ a, end=' | ')
print(((b and not b) or (not b and b)) == b ^ b, '\n')

# Operator 'is', 'is not'
# W przeciwieństwie do ==, operator 'is' nie testuje, czy zmienne mają jednakową wartość, 
# przeprowadzany jest test identyfikacyjny, czy objekt wskazuje na ten sam obszar w pamięci komputera, czy też nie

l1 = [1,2,3]
l2 = [1,2,3]
 
print(id(l1), id(l2)) # Output identyfikatory objektu

print(l1 == l2)       # True
print(l1 is l2)       # False
print(l1 is not l2)   # True
print(l1[1] != l2[1]) # False
print(l1[1] is l2[1]) # True

print()

## Tworzymy instrukcje warunkowe
# dane typu bool używane są między innymi w instrukcjach warunkowych i pętlach 
# Instrukcje warunkowe mają nastepujacą składnię: 

# >>> jeżeli (wartość logiczna warunku):   
# >>>     ciało warunku 1 
# >>> inaczej: 
# >>>     ciało warunku 2

# Zwróćmy uwagę na wcięcia blokowe, oraz dwukropki w instr. warunkowych w Pythonie 

if(x < y):
	warunek_txt = "x jest mniejsze od y"
else:
	warunek_txt = "x jest większe lub równe y"

print(warunek_txt)

# W przypadku gdy chcemy "przechwycić" więcej warunków użyjemy słowa kluczowego 'elif',
# w przeciwieństwie do 'if' oraz 'else', 'elif' może zostać użyte wielokrotnie w tym samym warunku.

# >>> jeżeli (wartość logiczna warunku):  
# >>>     ciało warunku 1
# >>> elif (jeżeli wartość logiczna poprzedniego warunku jest False):
# >>>     ciało warunku 2
# >>> elif (jeżeli wartość logiczna poprzednich warunków jest False):
# >>>     ciało warunku 3
# >>> inaczej: 
# >>>     ciało warunku 4

if(x < y):
	warunek_txt = "x jest mniejsze od y"
elif (x == y):
	warunek_txt = "x jest równe y"
else:
	warunek_txt = "x jest większe od y"

print(warunek_txt)

# możemy skorzystać z 'single line code notation', minimalizując przy tym miejsce
# Notacja: Zwróć uwagę, że nie stosujemy dwukropków
# >>> (A) jeżeli (B) inaczej (C) 

print("x jest mniejsze od y" if (x < y) else "x jest większe lub równe y")
