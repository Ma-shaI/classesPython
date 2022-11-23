# Task 1
import re

test = "1X, Test ABC 123 A1B2C3"
reg = r'(?<!\d)\d(?!\d)'
print(re.findall(reg, test))

# Task 2

# test = 'text from #START# till #END#'
# reg = r'#START#(\s+\w+\s+)#END#'
# print(re.findall(reg, test))

# Task 3

test = '12_34__56___45669_'
reg = r'\d+(?=_(?!_))'
print(re.findall(reg, test))
