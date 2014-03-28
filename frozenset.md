 * Frozenset
    * AKA: "Immutable Set"
    * Library: built-in
    * Description: Contains a series of non-duplicated elements. Attempts to insert a duplicate element are ignored
    * What Makes it Special: Like the `set` element is hashed as it is added, making *existence checks* 
      quite fast. `frozenset`s, however, are *immutable* (hence the "frozen" prefix).
    * Construction
        * `frozenset(iterable)`: using `frozenset()` to create a set comprised of the
          elements of `iterable`. Duplicate elements contained in `sequence` are
          silently removed.
    * Mutability: `immutable`
    * Ordering: `undefined`
