### `d.get(key[, default)`

Used to retrieve the value associated with key `key`. Optionally, a default
value, `default` is returned if `key` is not in `d` (rather than raising a
`KeyError`).

#### Returns
Roughly equivalent to:

~~~~{.py}
def get(key, default=None):
    if key in d:
        return d[k]
    elif default is not None:
        return default
    else:
        raise KeyError
~~~~

#### Raises

`KeyError` if `default` is not provided and `key` is not in `d`.

#### Examples

Get a key's value or `None` if the key isn't present
~~~~{.py}
for key in my_dictionary:
~~~~
