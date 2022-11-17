import re


def check_password(password):
    return re.findall(r'[A-z\d@_-]{6,18}$', password)


print(check_password('my-pss@w0rd'))


def check_number(number):
    s = re.findall(r'^M{0,3}(C|CC|CCC|CD|D|DC|DCC|DCCC|CM)?(X|XX|XXX|XL|L|LX|LXX|LXXX|XC)?'
                   r'(I|II|III|IV|V|VI|VII|VIII|IX)?$', number)
    if len(s) > 0:
        print(s)
        return 'это римское число'
    else:
        print(s)
        return "это не римское число"


print(check_number('MMDCCLXXII'))
print(check_number('CCCMMVIIVV'))
