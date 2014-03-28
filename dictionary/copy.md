### `d.copy()`

Make a *shallow* copy of `d`. The dictionary returned by `d.copy()` will have
the same references as `d`, not copies of the items.

#### Returns

A new `dict`, representing a *shallow* copy of `d`

#### Raises

N/A

#### Examples

Create copy of a dictionary

~~~~{.py}
d = {1: 'a', 2: 'b', 3: 'c'}
copied_dict = d.copy()
copied_dict # {1: 'a', 2: 'b', 3: 'c'}
d[1] = 'z'
copied_dict # {1: 'a', 2: 'b', 3: 'c'}
~~~~
