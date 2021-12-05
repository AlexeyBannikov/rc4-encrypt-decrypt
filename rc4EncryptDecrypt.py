import codecs

n = 8 #2**n=256

#key-scheduling algorithm
def KSA(key):
    key_length = len(key)
    S = list(range(2**n)) #S-box
    j = 0
    for i in range(2**n):
        j = (j + S[i] + key[i % key_length]) % 2**n
        S[i], S[j] = S[j], S[i] 
    return S

#pseudo-random generation algorithm
def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 2**n
        j = (j + S[i]) % 2**n 
        S[i], S[j] = S[j], S[i] 
        K = S[(S[i] + S[j]) % 2**n]
        yield K

def getKeyStream(key):
    S = KSA(key)
    return PRGA(S)

def encryptLogic(key, letter):
    key = [ord(i) for i in key]
    keystream = getKeyStream(key)
    res = []
    for i in letter:
        val = ("%02X" % (i ^ next(keystream))) #xor
        res.append(val)
    return ''.join(res)

def encrypt(key, letter):
    letter = [ord(i) for i in letter]
    return encryptLogic(key, letter)

def decrypt(key, cipherLetter):
    cipherLetter = codecs.decode(cipherLetter, 'hex_codec')
    res = encryptLogic(key, cipherLetter)
    return codecs.decode(res, 'hex_codec').decode('utf-8')
