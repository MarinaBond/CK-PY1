# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
func_ = ['bin', 'dec', 'hex', 'oct']
dict_ = [{'bin': bin(x), 'dec': x, 'hex': hex(x), 'oct': oct(x)} for x in range(16)]

pprint(dict_)