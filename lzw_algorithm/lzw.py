#!/usr/bin/python

from math import floor
from random import randint

def generate_esp_dist(n):
    caracteres = (("A", 12.53), ("B", 1.42), ("C", 4.68), ("D", 5.86), ("E", 13.68), ("F", 0.69), ("G", 1.01), ("H", 0.70), ("I", 6.25), ("J", 0.44), ("K", 0.01), ("L", 4.97), ("M", 3.15), ("N", 6.71), ("O", 8.68), ("P", 2.51), ("Q", 0.88), ("R", 6.87), ("S", 7.98), ("T", 4.63), ("U", 3.93), ("V", 0.90), ("W", 0.02), ("X", 0.22), ("Y", 0.90), ("Z", 0.52))

    acumulada = list()
    suma = 0.0
    text = ''
    for i in caracteres:
        suma += i[1]
        acumulada.append(suma)
    length = len(acumulada)

    for i in range(n):
        eleccion = randint(0, int(floor(acumulada[length-1])))
        for j in range(length):
            if acumulada[j] > eleccion:
                text += caracteres[j-1][0]
                break
    return text

class LZW:

    def __init__(self, dictionary):
        self.d = dictionary 
        self.p = 0

    def is_sufix(self, n):
        for i in self.d.values():
            if i == n:
                return True
        return False

    def get_char(self, n):
        for i in self.d.keys():
            if self.d[i] == n:
                return i
        return ""

    def encode(self, text):
        for char in text:
            if self.is_sufix(self.d[char]+self.p):
                self.p += self.d[char]
            else:
                yield self.d[self.get_char(self.p)]
                self.d[self.p+self.d[char]] = self.p
                self.p = self.d[char]
        yield self.d[self.get_char(self.p)]


def main():
    text = generate_esp_dist(10)
    chars = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    dictionary = dict()
    for i in range(len(chars)):
        dictionary[chars[i]] = i+1


    text = 'ABBABABAC'
    dictionary = {'A':1, 'B':2, 'C':3 }
    print 'input:', text
    lzw = LZW(dictionary)
    print 'output:', [i for i in lzw.encode(text)]

main()
