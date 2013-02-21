import time, random

def get_charstable(pattern):
    charstable = dict()
    length = len(pattern)
    for i in range(length):
        if not charstable.has_key(pattern[i]):
            charstable[pattern[i]] = (length-1-i)
    return charstable

def boyer_moore(string, pattern):
    charstable = get_charstable(pattern)
    length_pattern = len(pattern)
    length_string = len(string)
    i = length_pattern - 1# for the string
    j = length_pattern - 1# for the pattern
    shift = 0
    while i <= length_string - length_pattern:
        print len(string), len(pattern), i, j
        if string[i] == pattern[j]:
            shift += 1
            i -= 1
            j -= 1
            if shift == length_pattern-1:
                return i
        else:
            if string[i] in charstable:
                i += charstable[string[i]]
            else:
                i += length_pattern
            j = length_pattern - 1
            shift = 0

    return -1

def get_kmptable(string):
    pos = 2
    cnd = 0
    table = [0]*len(string)
    table[0] = -1
    table[1] = 0
    while pos < len(string):
        if string[pos-1] == string[cnd]:
            cnd += 1
            table[pos] = cnd
            pos += 1
        elif cnd > 0:
            cnd = table[cnd]
        else:
            table[pos] = 0
            pos += 1
    return table

def kmp(string, pattern):
    k = 0 #para el string
    i = 0 # para el pattern
    if len(string) >= len(pattern):
        table = get_kmptable(string)
        while k+i < len(string):
            if pattern[i] == string[k+i]:
                if i == len(pattern)-1:
                    return k
                i += 1
            else:
                k += i - table[i]
                if i > 0:
                    i = table[i]
    else:
        return -1

def generate_strings(patternt_length, text_length):
    letters = 'qwertyuiopasdfghjklzxcvbnm 1234567890'
    
    pattern = ''
    for i in range(patternt_length):
        pattern += random.choice(letters)

    text = pattern
    for i in range(text_length, patternt_length):
        if random.choice([True, False]):
            text = text + random.choice(letters)
        else:
            text = random.choice(letters) + text
    return pattern, text

def test(max_chars, fl='time_test.dat'):
    fl = open(fl , 'w')
    for i in range(2, max_chars+1):
        print i, 'de ', (max_chars)
        for j in range(2, i):
                pattern, string = generate_strings(j, i)

                before = time.time()
                boyer_moore(string, pattern)
                boyer_time = time.time()-before

                before = time.time()
                kmp(string, pattern) 
                kmp_time = time.time()-before

                fl.write(str(i)+' '+str(j)+' '+str(boyer_time)+' '+str(kmp_time)+'\n')
    fl.close()

def main():
    string = "anita lava la tina"
    pattern = "lava"
    print 'Boyer-Moore'
    print "String:", string
    print "Pattern:", pattern
    print "Position:", boyer_moore(string, pattern) 

    print 'Knuth-Morris-Pratt'
    print "String:", string
    print "Pattern:", pattern
    print "Position:", kmp(string, pattern) 

#main()
test(500)
