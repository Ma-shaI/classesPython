import re

def roma(ital):
    if re.findall(r'^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})+$'
                , ital) != [] and len(ital)!=0:
        print(ital, '-это римское число')
    else:
        print(ital, '-это набор знаков')

roma('MMDCCLXXII')
roma('')