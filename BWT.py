
def bwt_encode(text: str) -> str: 

    table = [[] for x in range(len(text))]
   
    n = len(text)
    c = 0 
    for i in range(n):
        ch = ""
        for y in range(n):
            ch = text[(y-i)%n]
            table[c].append(ch)
        c += 1 
    table = sorted(table)

    index = None
    for i in range(len(table)):
        if "".join(table[i]) == text:
            index = i 

    #prendre la derniere colonne donc le dernier element de chaque listes et concatener a l indice de l occurence du texte original
    concatened_res = str(index) + "".join([x[-1] for x in table])    

    
   
    return concatened_res

"""
    Burrows-Wheeler Transform (BWT) encoding.

    Étapes :
    1. Vérifier que le texte contient un caractère de fin unique (ex: '$').
    2. Générer toutes les rotations circulaires du texte.
    3. Trier les rotations dans l’ordre alphabétique (lexicographique).
    4. Construire la chaîne BWT en prenant le dernier caractère de chaque rotation triée.
    5. Retourner la chaîne BWT.
"""


#print(bwt_encode("banana"))       # ➝ 'annb$aa'

print(bwt_encode("mississippi$"))  # ➝ 'ipssm$pissii'
print(bwt_encode("abracadabra$"))  # ➝ 'ard$rcaaaabb'
print(bwt_encode("aaba$"))         # ➝ 'ab$a'
print(bwt_encode("aaaaa$"))        # ➝ 'aaaaa$'

print(bwt_encode("TEXTUEL")) #4UTELXTE 
print(bwt_encode("TEXTUELTEXTUEL"))
print(bwt_encode("banana$"))
