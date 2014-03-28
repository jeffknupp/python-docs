### `k in d`

Used to iterate over the keys, values, or both of the dictionary.

#### Returns

N/A

#### Raises

N/A

#### Examples

Iterate over keys

~~~~{.py}
for key in my_dictionary:
~~~~

Iterate over `(key, value)` tuples

~~~~{.py}
for key, value in my_dictionary.items():
~~~~


Iterate over values

~~~~{.py}
for value in my_dictionary.values():
~~~~

Check for existence

~~~~{.py}
haystack = {}
# ...
if 'needle' in haystack:
~~~~
