# Dictionary
 
## AKA
 
 "Associate Array", "Map", "Hash Map", "Unordered Map"

## Library

built-in

## Description

Contains a series of key->value mappings where the "key" is of any type that is *hashable* (meaning it has both a `__eq__()` and a `__hash__()` method).  The "value" may be of any type and value types need not be homogenous.

## What Makes it Special

The underlying implementation is that of a hash table, so checks for existence are quite fast. 

## Construction 

* `{}`: pair of braces for empty dictionary 
* `{1:2, 3:4}`: comma-separated list of the form `key: value` enclosed by braces
* `dict(one=2, three=4)`: using `dict()` with *keyword arguments* mapping keys to values (where `one` and `two` are valid identifiers)
* `dict([(1, 2), (3, 4)])`: using `dict()` with an iterable containing iterables with exactly two objects, the key and value
* `dict(zip([1, 3], [2, 4]))`: using `dict()` with two iterables of equal length; the first contains a list of keys and the second contains their associated values.
* `dict({1:2, 3:4})`: using `dict()` with the literal form as an argument. This is silly. Why would you want this?

## Mutability

`mutable`

## Ordering

`undefined`

## When to Use It

When describing what you want to do, if you use the word "map" (or "match"), chances are good 
you need a dictionary. Use whenver a mapping from a key to a value is required. 

## Example Usage 

`state_captials={'New York': 'Albany'}` 

"New York" is a *key* and "Albany" is a *value*. This allows us to retrieve a state's capital if
we have the state's name by doing `capital = state_captials[state]`

## Methods and Uses
