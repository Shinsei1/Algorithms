#LZ78
#représentation de base du dictionnaire
def lpz_simplified(texte: str):
    tab = []
    i = 0
    while i < len(texte):
        saut = 1
        if texte[i] not in tab:
            tab.append(texte[i])
            i += 1
        else:
            while (i + saut) <= len(texte) and texte[i:i + saut] in tab:
                saut += 1
            tab.append(texte[i:i + saut])
            i += saut
                
    return tab

sequence = "BANANA"    
print(lpz_simplified(sequence))
a = lpz_simplified(sequence)

#good notation for lpz algorithms, this function act as a translator of the previous result 
#def lpz78_(result):
    
    
#print(lpz78_(a))
    