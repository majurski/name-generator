#This simple name generator 
#You can create any name by given string
import random

#base string for creating the name
example = "abcdefghklmopqrstuvwxyz"

def gen(source):
   return random.choice(source)

a = []

#the lenght of the name, number of letters 
for i in range(5):
   a.append(gen(example))

name = ''.join(a)
      
print(f'Днес името е {name}')