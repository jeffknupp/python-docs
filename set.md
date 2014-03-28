* Set
    * AKA: "Hash Set", "Unordered Set"
    * Library: built-in
    * Description: Contains a series of non-duplicated elements. Attempts to insert a duplicate element are ignored
    * What Makes it Special: Each element is hashed as it is added, making *existence checks* 
      quite fast. This also prevents multiple copies of the same element from
      being added.
    * Construction
        * `set(iterable)`: using `set()` to create a set comprised of the
          elements of `iterable`. Duplicate elements contained in `sequence` are
          silently removed.
        * `{1, 2}`: comma-separated list of initital values surrounded by braces
    * Mutability: `mutable`
    * Ordering: `undefined`
