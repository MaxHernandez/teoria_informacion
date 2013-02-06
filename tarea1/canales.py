import random, sys, math

class Simulator:
# frecuencias = [frecuencia de 0, frecuencia de 1]
# probabilidad de = [[enviar 0 y recibir 0, enviar 0 y recibir1], [enviar 1 y recibir 0, enviar 1 y recibir1]]
    def __init__(self, frecuencias, probabilidadrecived):
        self.frecuencias = frecuencias
        self.Q = probabilidadrecived

    def generate_word(self, longitud):
        word = []

        for i in range(longitud):
            if random.random() > self.frecuencias[0]:
                word.append(0)
            else:
                word.append(1)
        return word

    def word_transmission(self, word):
        word_recived = list()
        for i in range(len(word)):
            aleatorio = random.random()
            if aleatorio > self.Q[word[i]][word[i]]:
                if word is 0:
                    word_recived.append(1)
                else:
                    word_recived.append(0)
            else:
                word_recived.append(word[i])
        return word_recived

    def generate_population(self, lonword, nPopulation):
        exitos = 0
        for i in range(nPopulation): 
            word = self.generate_word(lonword)
            recived = self.word_transmission(word)
            if comp(word, recived):
                exitos += 1

        return float(exitos)/nPopulation

def pstr(word):
    nueva = ""
    for i in word:
        nueva += str(i)
    return nueva

def comp(word1, word2):
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return False
    return True

def main():
    """
    Parametros: 
    sys.argv[1] -> nombre del archivo
    sys.argv[2] -> longitud maxima de word
    sys.argv[3] -> numero de intentos por cada longitud de word
    sys.argv[4] -> probabilidad de aparicion de 0
    sys.argv[5] -> probabilidad de enviar un 0 con exito
    sys.argv[6] -> probabilidad de enviar un 1 con exito
    """
    fl = open(sys.argv[1], "w")
    sim = Simulator([float(sys.argv[4]), (1.0-float(sys.argv[4]))], [[float(sys.argv[5]), (1.0-float(sys.argv[5]))], [(1.0-float(sys.argv[6])), float(sys.argv[6])]])

    for i in range(1, int(sys.argv[2])+1):
        fl.write(str( sim.generate_population(i, int(sys.argv[3])) )+" "+str(i)+"\n")
    fl.close()

main()
