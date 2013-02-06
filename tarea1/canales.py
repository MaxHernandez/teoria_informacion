import random, sys, math

class Simulator:
# frequencies = [frequency of 0, frequency of 0 1]
# probRecived = [[send 0 and recive 0, send 0 and recive 1], [send 1 and recive 0, send 1 y recive 1]]
    def __init__(self, frequencies, probRecived):
        self.frequencies = frequencies
        self.Q = probRecived

    def generate_word(self, lon):
        """ This function use Bernoulli trials to generato each symbol of
            a "lon" length word
	"""
        word = []
        for i in range(lon):
        #Use the frequency vector probabilities to make the Bernoulli trial
            if random.random() > self.frequencies[0]:
                word.append(0)
            else:
                word.append(1)
        return word

    def word_transmission(self, word):
        """ This function use another Bernoulli trial to simulate an error
            on word transmission
        """
        word_recived = list()
        for i in range(len(word)):
            aleatorio = random.random()
            # each symbol has a row in the Q matrix and each row have a 
            # probability to change or no to change in transmission so that's
            # what we use to generate the Bernoully trial
            if aleatorio > self.Q[word[i]][word[i]]:
                if word is 0:
                    word_recived.append(1)
                else:
                    word_recived.append(0)
            else:
                word_recived.append(word[i])
        return word_recived

    def generate_population(self, lonword, nPopulation):
	""" This function make transsmition and return the frequency of success"""
        exitos = 0
        for i in range(nPopulation): 
            word = self.generate_word(lonword)
            recived = self.word_transmission(word)
            if comp(word, recived):
                exitos += 1

        return float(exitos)/nPopulation

def pstr(word):
    """ Secundary function to obtain a string representation of a vector word"""
    nueva = ""
    for i in word:
        nueva += str(i)
    return nueva

def comp(word1, word2):
    """Make a word comparison"""
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return False
    return True

def get_mean(vector):
    mean = 0.0
    for i in vector:
        mean += i
    return (mean/float(len(vector)))

def get_sd(vector):
    """Standard deviation """
    mean = get_mean(vector)
    sd = 0.0
    for i in vector:
        sd += (i-mean)**2
    sd = (sd/float(len(vector)))**0.5
    return mean, sd

def main():
    """
    Parametros: 
    sys.argv[1] -> Output file
    sys.argv[2] -> word maximun length
    sys.argv[3] -> number of messages sended fo each word length
    sys.argv[4] -> frequecy of 0 
    sys.argv[5] -> Send a 0 with success probability
    sys.argv[6] -> Send a 1 with success probability
    """
    fl = open(sys.argv[1], "w")
    sim = Simulator([float(sys.argv[4]), (1.0-float(sys.argv[4]))], [[float(sys.argv[5]), (1.0-float(sys.argv[5]))], [(1.0-float(sys.argv[6])), float(sys.argv[6])]])

    values = list()
    for i in range(1, int(sys.argv[2])+1):
        values.append( sim.generate_population(i, int(sys.argv[3])) )

    mean, sd = get_sd(values)
    for i in range(1, int(sys.argv[2])+1):
        fl.write(str( values[i-1] )+" "+str(i)+" "+str(mean)+" "+str(sd)+"\n")


    fl.close()

main()
