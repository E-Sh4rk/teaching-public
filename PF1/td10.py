# To run with Python >= 3.9
import math

## ========= EX 1 =========

def bruteforce_scytale(txt, diam_max):
    for i in range(1,diam_max):
        str2 = [ txt[(k*i)%len(txt)] for k in range(len(txt)) ]
        print(str(i)+":"+"".join(str2))

# bruteforce_scytale("prorrotnecurdperoeusdubicevosycenethrdnaiuirlfnaoefbmu_rael_ette", 10)

## ========= EX 2 =========

def pos_in_alphabet(c):
    return ord(c) - ord("a")

def letter_at_pos(p):
    return chr(p + ord("a"))

def encode_cesar(txt, offset):
    res = ""
    for c in txt:
        new_pos = (pos_in_alphabet(c)+offset)%26
        res += letter_at_pos(new_pos)
    return res

def decode_cesar(txt, offset):
    return encode_cesar(txt, -offset)

# print(encode_cesar("unrondpastoutafaitclos", 4))

def bruteforce_cesar(txt):
    for i in range(0,26):
        print(str(i) + ":" + decode_cesar(txt, i))
    
# bruteforce_cesar("gaiatksginotkgaiatjuiasktzvuaxrkdgsktjkvlat")

def distance(distr1, distr2):
    return sum([ (distr1[i] - distr2[i])**2 for i in range(len(distr1)) ])

def shift_distr(distr, k):
    return [ distr[(i+k)%len(distr)] for i in range(len(distr)) ]

freq_french =  [8.13, 0.93, 3.15, 3.55, 15.10, 0.96, 0.97, 1.08, 6.94, 0.71, 0.16, 5.68, 3.23, 6.42, 5.27, 3.03, 0.89, 6.43, 7.91, 7.11, 6.05, 1.83, 0.04, 0.42, 0.19, 0.21]
freq_english = [8.55, 1.60, 3.16, 3.87, 12.10, 2.18, 2.09, 4.96, 7.33, 0.22, 0.81, 4.21, 2.53, 7.17, 7.47, 2.07, 0.10, 6.33, 6.73, 8.94, 2.68, 1.06, 1.83, 0.19, 1.72, 0.11]

def decrypt_cesar(txt, freq_ref):
    occ = [0]*26
    for c in txt:
        occ[pos_in_alphabet(c)] += 1
    freq = [ n*100/len(txt) for n in occ ]
    shifts_scores = [ distance(freq_ref, shift_distr(freq, i)) for i in range(0, 26) ]
    best_match = shifts_scores.index(min(shifts_scores))
    return (letter_at_pos(best_match), decode_cesar(txt, best_match))

# print(decrypt_cesar("gaiatksginotkgaiatjuiasktzvuaxrkdgsktjkvlat", freq_french))

## ========= EX 3 =========

def find_key_length(txt, length_factors):
    res = []
    map = { }
    for i in range(0,len(txt)-length_factors):
        current = txt[i:i+4]
        if current in map:
            #print(current)
            res.append(i-map[current])
        map[current] = i
    return math.gcd(*res)

txt = "cliiyaatpiencueugaetkfvrr\
dwsmreaqmsbcvlodwlyvhoijd\
kiudpankyeytvwfdaxanoztex\
wveepixoatzwhsaeokyebalof\
ugeijdfltdpwrvzfdpasnvrob\
jucpadmktredgpstvmebqlwrj\
hosfenyiwawlwtaeoztzeidbj\
aggenjqtyrtrifdrkhsafetbt\
rmyodaaljsryvrokslcvddpwr\
vjpyvkewiowbzecztkvqaxrix\
alfvrrkazijdodpwryrddimgy\
khsugukffdpwbveeqmksviidz\
atv"

# print(find_key_length(txt, 4))

def decrypt_vigenere(txt, key_length, freq_ref):
    cesars = [ txt[i::key_length] for i in range(0, key_length) ]
    decrypted = [ decrypt_cesar(cesar, freq_ref) for cesar in cesars ]
    (key, decrypted) = zip(*decrypted)
    key = "".join(key)
    res = ""
    for i in range(0, len(txt)):
        res += decrypted[i%key_length][i//key_length]
    return (key, res)

# print(decrypt_vigenere(txt, find_key_length(txt, 4), freq_french))
# print(decrypt_vigenere(txt, find_key_length(txt, 4), freq_english))
