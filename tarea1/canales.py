import random, sys, math

class Simulador:
# frecuencias = [frecuencia de 0, frecuencia de 1]
# probabilidad de = [[enviar 0 y recibir 0, enviar 0 y recibir1], [enviar 1 y recibir 0, enviar 1 y recibir1]]
    def __init__(self, frecuencias, probabilidadRecibida):
        self.frecuencias = frecuencias
        self.Q = probabilidadRecibida

    def generar_palabra(self, longitud):
        palabra = []

        for i in range(longitud):
            if random.random() > self.frecuencias[0]:
                palabra.append(0)
            else:
                palabra.append(1)
        return palabra

    def transmitir_palabra(self, palabra):
        palabra_recibida = list()
        for i in range(len(palabra)):
            aleatorio = random.random()
            if aleatorio > self.Q[palabra[i]][palabra[i]]:
                if palabra is 0:
                    palabra_recibida.append(1)
                else:
                    palabra_recibida.append(0)
            else:
                palabra_recibida.append(palabra[i])
        return palabra_recibida

    def generar_poblaciones(self, lonPalabra, nPoblaciones):
        exitos = 0
        for i in range(nPoblaciones): 
            palabra = self.generar_palabra(lonPalabra)
            recibida = self.transmitir_palabra(palabra)
            if comp(palabra, recibida):
                exitos += 1

        return float(exitos)/nPoblaciones

def pstr(palabra):
    nueva = ""
    for i in palabra:
        nueva += str(i)
    return nueva

def comp(palabra1, palabra2):
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            return False
    return True

def main():
    """
    Parametros: 
    sys.argv[1] -> nombre del archivo
    sys.argv[2] -> longitud maxima de palabra
    sys.argv[3] -> numero de intentos por cada longitud de palabra
    sys.argv[4] -> probabilidad de aparicion de 0
    sys.argv[5] -> probabilidad de enviar un 0 con exito
    sys.argv[6] -> probabilidad de enviar un 1 con exito
    """
    fl = open(sys.argv[1], "w")
    sim = Simulador([float(sys.argv[4]), (1.0-float(sys.argv[4]))], [[float(sys.argv[5]), (1.0-float(sys.argv[5]))], [(1.0-float(sys.argv[6])), float(sys.argv[6])]])

    for i in range(1, int(sys.argv[2])+1):
        fl.write(str( sim.generar_poblaciones(i, int(sys.argv[3])) )+" "+str(i)+"\n")
    fl.close()

main()
