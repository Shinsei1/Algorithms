
"""TESTS"""
"""
p = phrase
p = p.split(" ")
p = list(p)
dico = {}
c = 0
for x in range(len(p)):   
    if not p[x] in dico.keys():
        dico[p[x]] = c  
        c+=1
encoded = []
for x in p:
    if x in dico:
        encoded.append(dico[x])
binary_encoded = []
for y in encoded:
    binary_encoded.append(bin(y)[2:])
"""

#n = 14
#s = ""
#while n>0:
#    r = n%2
#    s+=str(r)
#    n= n//2 
#print(s)
#print(bin(14))


"""FONCTION"""


def dict_encoding(text:str)->list:
    p = text.split(" ")
    dico = {}
    c = 0
    for x in range(len(p)):   
        if not p[x] in dico.keys():
            dico[p[x]] = c 
            c+=1
    encoded = []
    for x in p:
        if x in dico:
            encoded.append(dico[x])
    return encoded

print(dict_encoding("apple âpple banana banâna and apple âpple in the market. People said the âpple was sweeter than the apple, while the banâna looked strange next to the banana."))
print(dict_encoding("apple banana apple orange cherry watermelon watermelon"))





"""BINARY FUNCTION"""
def binary_convertion(n:int)->str:
    if n == 0:
        return "0"
    s = ""
    while n>0:
        r = n%2
        s+=str(r)
        n= n//2 
    return s[::-1] 


"""DICT WITH BINARY ENCODING"""

def dict_encoding_binary(text:str)->list:
    p = text.split(" ")
    #p = list(p)
    dico = {}
    c = 0
    for x in range(len(p)):   
        if not p[x] in dico.keys():
            dico[p[x]] = c  
            c+=1
    encoded = []
    for x in p:
        if x in dico:
            encoded.append(dico[x])
    binary_encoded = [binary_convertion(x) for x in encoded]
    #return [int(x) for x in binary_encoded] # pr avoir le resultat avc des ints dns le tab
    return binary_encoded

print(dict_encoding_binary("apple banana apple orange cherry watermelon"))
#idée pr la reconstruction: a chaque mot, ajouter un espace apres celui-ci

