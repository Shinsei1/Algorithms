
# 1. Majuscules A-Z
alphabet_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# 2. Minuscules a-z
alphabet_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]

# 3. Lettres a-z + A-Z
alphabet_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
                   [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# 4. Chiffres 0-9
alphabet_digits = [str(i) for i in range(10)]

# 5. Lettres + chiffres
alphabet_alphanum = [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
                    [str(i) for i in range(10)]

# 6. Lettres + chiffres + ponctuation
import string
alphabet_full = list(string.ascii_letters + string.digits + string.punctuation)

# 7. Tous les octets (0–255), pour compression binaire
alphabet_bytes = [i for i in range(256)]



#methode sans range
"""
def move_to_front(text: str, alphabet: list) -> list:
    MTF_tab = []
    for char in text:
        index = alphabet.index(char)
        MTF_tab.append(index)
        alphabet.pop(index)
        alphabet.insert(0,char)
    return MTF_tab
"""       

def move_to_front(text: str, alphabet: list) -> list:
    MTF_tab = []
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                MTF_tab.append(j)
                alphabet.pop(j)
                alphabet.insert(0,text[i])
    return MTF_tab


alph_exo = alphabet_upper

#texte = "ABCDEBANANAAPPLEBANANA"

#print(move_to_front(texte,alph_exo))

texte = "EEEEEAAAABBBAAA"

print(move_to_front(texte,alphabet_upper))

