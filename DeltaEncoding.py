


def delta_encoding(data_list:list)->list:
    delta_encoded = [data_list[0]]
    for i in range(len(data_list)):
        if i < len(data_list)-1:
            delta_encoded.append(data_list[i+1]-data_list[i])
    return delta_encoded



def delta_decoding(delta_encoded_list:list)->list:
    delta_decoded = [delta_encoded_list[0]]
    for i in range(len(delta_encoded_list)):
        if i > 0:
            delta_decoded.append(delta_decoded[-1]+delta_encoded_list[i])
    return delta_decoded



print(delta_encoding([100, 105, 110, 120]))         # [100, 5, 5, 10]
print(delta_decoding([100, 5, 5, 10]))              # [100, 105, 110, 120]

print(delta_encoding([1, 1, 2, 3, 5, 8, 13]))       # [1, 0, 1, 1, 2, 3, 5]
print(delta_decoding([1, 0, 1, 1, 2, 3, 5]))        # [1, 1, 2, 3, 5, 8, 13]

print(delta_encoding([50]))                        # [50]
print(delta_decoding([50]))                        # [50]




