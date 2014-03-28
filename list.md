* List
    * AKA: "Array", "Vector"
    * Library: built-in
    * Description: Contains a series of (possibly) heterogeneous values
    * What Makes it Special: A work-horse data structure, the `list` is notable
      for its overall utility. It provides storage for a mutable sequence of
      values and iteration order is well-defined. Appending to the end of a
      `list` is an extremely fast operation. Removing or inserting from the
      middle is a good deal slower.
    * Construction
        * `[]`: pair of empty square-brackets for empty list
        * `[1, 2, 3]`: comma-separated list containing initial values
        * `[element for element in interable]`: as list comprehension over
          existing iterable
        * `list()`: using `list()` to create an empty list
        * `list(iterable)`: using `list()` with an iterable to be used as the initial
          series of values 
    * Mutability: `mutable`
    * Ordering: `defined`
    * When to Use It: Whenever a list of values is needed, especially if the ordering 
      of values is important.
    * Example Usage: `stooges = ['Larry', 'Moe', 'Curly']` Each element can be
      retrieved using its zero-based index in the list (i.e. "Moe" is index `1`). 
