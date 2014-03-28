### `dict.fromkeys(seq[, value])`

Create a new dictionary with the same keys as `seq`. If `value` is provided,
each item's value is set to `value`. If `value` is not set, all item values are set to
`None`

#### Returns

N/A

#### Raises

N/A

#### Examples

Create a dictionary from a list with all values initialized to 0

~~~~{.py}
my_list = [1, 2, 3]
my_dictionary = dict.fromkeys(my_list, 0)
my_dictionary # {1: 0, 2: 0, 3: 0}
~~~~

Create a dictionary from a dictionary with all values automatically initialized to `None`

~~~~{.py}
my_dictionary = {1: 1, 2: 2, 3: 3}
new_dictionary = dict.fromkeys(my_dictionary)
my_dictionary # {1: None, 2: None, 3: None}
~~~~
