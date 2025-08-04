def RLE(text, first=0, first_value=None):
    first_value = text[first]  
    take = []
    for i in range(first, len(text)):
        if text[i] == first_value:
            take.append(text[i])
        else:
            return "".join([str(len(take))] + [str(take[0])]) + "".join([str(x) for x in RLE(text, first=i, first_value=text[i])])
    result = [str(len(take))] + [take[0]]
    return result

print(RLE("====))))(((((((())))))))"))
print(RLE("aannnnn"))