
def get_multiplied_digts(number):
    str_number = str(number)
    str_number = str_number.strip('0')
    fist = int(str_number[0])
    if len(str_number) == 1:
        return fist
    else:
        return fist * get_multiplied_digts(str_number[1:])
    
    
print(get_multiplied_digts(2550))
print(get_multiplied_digts(40045))
print(get_multiplied_digts(1001010))
print(get_multiplied_digts(231))