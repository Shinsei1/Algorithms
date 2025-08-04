#AAABBBCCD -> 3A3B2C1D

def RLE(text, first=0, first_value=None):
    #if first_value is None:
    first_value = text[first]  

    take = []
    for i in range(first, len(text)):
        if text[i] == first_value:
            take.append(text[i])
        else:
            return [len(take)] + take + RLE(text, first=i, first_value=text[i])
    
    return [len(take)] + take
"""

def RLE(text,first=0,first_value=None):
    take = []
    if first_value is None:
        first_value = text[first]
        
    for i in range(first,len(text)):
        if text[i] == first_value:
            
            take.append(text[i])
        else:
            return [len(take)] + take + RLE(text=text,first=i,first_value=text[i])
            
    return [x for x in take if x != "0"]
"""
print(RLE("AAABBBCCHHHDGGGEUUUDYYY"))
"""   


def clean(text:str)->str:
    text = RLE(text)
    cleaned = []
    for x in range(len(text)):
        try:
            if type(text[x]) == int:
                cleaned.append(text[x])
                cleaned.append(text[x+1])
        except Exception as e:
            pass 
    cleaned = "".join([str(x) for x in cleaned])
    return cleaned


def clean_remake(text:str)->str:
    text = RLE(text)
    cleaned = []
    for x in range(len(text)):      
        if isinstance(text[x],int): #plus intéressant car ne crée aucune erreur (isinstance prend l element et verifie si il correspond au type donné)
                cleaned.append(text[x])
                cleaned.append(text[x+1])
    cleaned = "".join([str(x) for x in cleaned])
    return cleaned
#donc tant que je trouve du A je continue, des que je trouve autre chose je m arrete et met le compteur first = a l indice 
print(clean("AAABBBBCCCAA"))
print(clean_remake("AAABBBBCCCAADDDSSSEARTUUUUUU"))

"""
"""
Version propre:
text = "AAABBBBCCCAA"

def v(text, first=0, first_value=None):
    if first_value is None:
        first_value = text[first]

    take = []

    for i in range(first, len(text)):
        if text[i] == first_value:
            take.append(text[i])
        else:
            # Fin du groupe → appel récursif sur la suite
            return [len(take)] + take + v(text, first=i, first_value=text[i])

    # Si on arrive ici : fin de chaîne atteinte → dernier groupe
    return [len(take)] + take

print(v(text))

"""