
def encode_large_number_by_set(NumberSet:list,n:int,encoded=[])->list:
    MAX_SET = max(NumberSet)
    if n < MAX_SET:
        return encoded+[n] 
    else:
        n = n - MAX_SET
        encoded += [MAX_SET]
        return encode_large_number_by_set(NumberSet,n,encoded=encoded)


print(encode_large_number_by_set([0,1,2,3,4,5,6,7,8,9,10],800,[]))
print(encode_large_number_by_set([0,1,2,3,4],10))
print(encode_large_number_by_set([0,1,2,3,4,5,6,7,8,9,10],49,[]))
