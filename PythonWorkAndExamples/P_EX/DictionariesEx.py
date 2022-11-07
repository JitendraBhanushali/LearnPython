""" --------------------- Dictionaries --------------------"""
tel = {'jack': 4098, 'sape': 4139,'ack': 198}
print(tel)
tel['guido'] = 4127
print(tel)
print(tel['jack'])


del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print('guido' in tel)

print('jack' not in tel)


# tel1 = {'jack': 4098, 'sape': 4139, 'ack': 198}
# print(sorted(tel1))

""" The dict() constructor builds dictionaries directly from sequences of key-value pairs: """
# dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(dict.values())

a = {x: x**2 for x in (2, 4, 6)}
print(a)