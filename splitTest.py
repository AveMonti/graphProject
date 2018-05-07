import ast

# def stringToDictionary(s, pairSeparator, keyValueSeparator):
#     pairs = s.split(pairSeparator)
#     return dict(pair.split(keyValueSeparator) for pair in pairs)


# s = "0: [1,2,3]; 1: []; 2: [1]; 3: [4,5];4: [3,5]; 5: [3,4,7]; 6: [8]; 7: [];8: [9]; 9: []"
# D = stringToDictionary(s, ';', ':')

s = "{0: [1,2,3], 1: [], 2: [1], 3: [4,5],4: [3,5], 5: [3,4,7], 6: [8], 7: [],8: [9], 9: []}"
d = ast.literal_eval(s)
print(d)
print(type(d))
