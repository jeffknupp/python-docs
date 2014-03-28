### `del k[d]`

Used to remove a value from a dictionary

#### Returns

N/A

#### Raises

`KeyError` if key is not in dictionary

#### Examples

Delete entry with key 'hello'

~~~~{.py}
my_dictionary = {'hello': 1, 'goodbye': 2}
del my_dictionary['hello']
print(my_dictionary)
# {'goodbye': 2}
~~~~
