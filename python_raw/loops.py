#!/usr/bin/python3

## Loops - pętle
# Powtórzenia nazywa się w językach programowania pętlami (loops), wielokrotne wykonywanie zdefiniowanych operacji.
# w Pythonie wyróżnia się dwa rodzaje pętli: while i for.

print(list(range(10)))
print(sum(range(10)))

## Pętla for  
# Opercje na liczbach
counter = 0
for x in range(3):
  counter = counter + 1
  # print(x, counter)
print(counter)

# korzystamy z funkcji range() oraz argumentów: start, stop, and step, by przejść prez przedział liczb 1 do 10
for i in range(1, 10, 2):
  print(i, end=', ')       # Output nieparzyste liczby miedzy 1 a 10"


print("range() petla for - przyklad do obliczania pierwiastka kwadratowego")
for i in range(1, 5):
  square = i**2
  print("square of", i, "is", square)

# For..Else
for x in range(3):
  print(x)
else:
  print('Final x = %d' % (x))

# Instrukcje "break" i "continue"
# break jest używany do zakończenia pętli for i while, 
# continue pozwala opuścić blok instrukcji i wrócić do pętli

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print (n, 'równe', x, '*', int(n/x))
      break
  else:
    print (n, 'jest liczbą pierwszą')

# Operacje na napisach
string = "Hello Tomek"
for x in string:
  print(x)

# Operacje na listach
li_users = ["bartek", "nina", "tomek"]

for x in li_users:
  print(x)

# Operacje na słownikach
dict_stud1 = {'name':'bartek', 'exam':3, 'active': True}

for key in dict_stud1:
    print(key, '->', dict_stud1[key])

dict_stud2 = {'name':'nina', 'exam':2, 'active': False}
dict_stud3 = {'name':'tomek', 'exam':3.5, 'active': True}

# Operacje na zróżnicowanym typie danych
li_dict_studs = [dict_stud1,dict_stud2,dict_stud3]

for x in li_dict_studs:
  print(x)

# Zagnieżdżona pętla for (nested for loop)
for x in li_dict_studs:
  for key in x:
    print(key, '->', x[key])

## Pętla while 
# wykonywana jest dopóki pewien warunek logiczny jest spełniony

count = 0
while count < 3:     
  print(count)  
  count = count + 1    

while True:
  break

while(True): 
  if count<5:
    count += 1       # Ma to taki sam efekt jak count = count + 1
    print(count)
  else:
    break

i=0
while count==5 and counter<10:
  i+=1
  print('\nwhile', i)
  break
