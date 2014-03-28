### `d[key]`

Used to access the value corresponding to the key `key` in `d`.

#### Returns

Value associated with the key (heterogenous)

#### Raises

`KeyError` when `key` is not a member of `d`.

#### Examples

~~~~{.python}
capitals = {'New York': 'Albany'}`
capital_of_ny = capitals['New York']`
print capital_of_ny`
'Albany'
~~~~
