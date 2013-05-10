import random, sys, math

class Simulator:

    def __init__(self, frequencies, probRecived):
        self.frequencies = frequencies
        self.Q = probRecived
        
    def check_hamming_error(self, word):
        check_word = word[:]
        word = word[:]

        for i in range(len(word)):
            comp = math.log((i+1)**2, 2)
            if comp == int(comp):
                saltos = i+1
                bits_counter = 0
                saltos_counter = 1
                bandera = True
                for j in range(i+1, len(word)):
                    if saltos_counter == saltos:
                        saltos_counter = 0
                        if bandera == True:
                            bandera = False
                        else:
                            bandera = True

                    if bandera == True:
                        if word[j] == 1:
                            bits_counter += 1
                    saltos_counter += 1

                if bits_counter%2 == 0:
                    check_word[i] = 0
                else:
                    check_word[i] = 1

        res = exor(word, check_word)
        error_pos = 0
        for i in range(len(res)):
            if res[i] == 1:
                error_pos += i+1

        if error_pos == 0 or error_pos > len(word):
            return word
        else:
            if word[error_pos-1] == 1:
                word[error_pos-1] = 0
            else:
                word[error_pos-1] = 1
            return word
                    

    def create_hamming_code(self, word):
        new_word = list()
        length = len(word)
        pos_word = 0
        pos_new = 1
        new_word.append(None)
        while pos_word < length:
            comp = math.log((pos_new+1)**2, 2)
            if comp == int(comp):
                new_word.append(None)
            else:
                new_word.append(word[pos_word])
                pos_word += 1
            pos_new += 1
        
        for i in range(len(new_word)):
            if new_word[i] == None:
                saltos = i+1
                bits_counter = 0
                saltos_counter = 1
                bandera = True
                for j in range(i+1, len(new_word)):
                    if saltos_counter == saltos:
                        saltos_counter = 0
                        if bandera == True:
                            bandera = False
                        else:
                            bandera = True

                    if bandera == True:
                        if new_word[j] == 1:
                            bits_counter += 1
                    saltos_counter += 1

                if bits_counter%2 == 0:
                    new_word[i] = 0
                else:
                    new_word[i] = 1
        return new_word

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
        return self.create_hamming_code(word)

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

def exor(word1, word2):
    res = list()
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            res.append(0)
        else:
            res.append(1)
    return res
    
def comp(word1, word2):
    """Make a word comparison"""
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return False
    return True

def pstr(word):
    """ Secundary function to obtain a string representation of a vector word"""
    nueva = ""
    for i in word:
        nueva += str(i)
    return nueva

def main():
    """
    Parametros: 
    sys.argv[1] -> frequecy of 0 
    sys.argv[2] -> Send a 0 with success probability
    sys.argv[3] -> Send a 1 with success probability
    """
    frequency_zero = 0.50
    success_zero = 0.99
    success_one = 0.99
    sim = Simulator([float(frequency_zero), (1.0-float(frequency_zero))], [[float(success_zero), (1.0-float(success_zero))], [(1.0-float(success_one)), float(success_one)]])
#    sim = Simulator([float(sys.argv[1]), (1.0-float(sys.argv[1]))], [[float(sys.argv[2]), (1.0-float(sys.argv[2]))], [(1.0-float(sys.argv[3])), float(sys.argv[3])]])
    succesful_words = 0
    fixed_words = 0
    not_fixed_word = 0

    word = [0,1,0,1,0]
    recived = [0, 1, 1, 0, 1, 0, 1, 0, 0]
    checked = sim.check_hamming_error(recived)
    print 'Example with one error'
    print 'Original Word:', pstr(word)
    print 'Recived word: ', pstr(recived)
    print 'Checked word: ', pstr(checked)

    total_words = 250
    print '\ngenerating', total_words, 'words...'
    for i in range(total_words):
        word = sim.generate_word(20)
        recived = sim.word_transmission(word)
        checked = sim.check_hamming_error(recived)

        if comp(word, recived):
            succesful_words += 1
        else:
            if comp(checked, recived):
                fixed_words += 1
            else:
                not_fixed_word  += 1
    print "Words without errors:", succesful_words
    print "Fixed words:", fixed_words
    print "Not fixed words:", not_fixed_word

def experiment():
    fl = open("output.dat", "w")

    frequency_zero = 0.50
    success_zero = 0.99
    success_one = 0.99

    change = 0.001

    while success_zero > 0.5:
        sim = Simulator([float(frequency_zero), (1.0-float(frequency_zero))], [[float(success_zero), (1.0-float(success_zero))], [(1.0-float(success_one)), float(success_one)]])

        success_zero -= change
        success_one -= change

        succesful_words = 0
        fixed_words = 0
        not_fixed_word = 0        
        total_words = 100
        for i in range(total_words):
            word = sim.generate_word(20)
            recived = sim.word_transmission(word)
            checked = sim.check_hamming_error(recived)

            if comp(word, recived):
                succesful_words += 1
            else:
                if comp(checked, recived):
                    fixed_words += 1
                else:
                    not_fixed_word  += 1
        fl.write(str(success_zero)+' '+str(succesful_words)+' '+str(fixed_words)+' ' +str(not_fixed_word)+'\n')
    fl.close()

def experiment2():
    fl = open("output.dat", "w")

    frequency_zero = 0.50
    success_zero = 0.7
    success_one = 0.7
    change = 0.001

    nbits = 0
    while nbits < 1000:
        nbits += 1
        sim = Simulator([float(frequency_zero), (1.0-float(frequency_zero))], [[float(success_zero), (1.0-float(success_zero))], [(1.0-float(success_one)), float(success_one)]])

        succesful_words = 0
        fixed_words = 0
        not_fixed_word = 0        
        total_words = 100
        for i in range(total_words):
            word = sim.generate_word(20)
            recived = sim.word_transmission(word)
            checked = sim.check_hamming_error(recived)

            if comp(word, recived):
                succesful_words += 1
            else:
                if comp(checked, recived):
                    fixed_words += 1
                else:
                    not_fixed_word  += 1
        fl.write(str(nbits)+' '+str(succesful_words)+' '+str(fixed_words)+' ' +str(not_fixed_word)+'\n')
    fl.close()

#main()
experiment()
experiment2()
