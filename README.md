# AdventOfCode2017
Python code to solve daily puzzles of http://adventofcode.com/2017

Code is tested with Python 3.6.3 (Anaconda distribution) on Win10.  Developed with VSCode.

## Days
* Day 1:  Simple iteration
* Day 2:  Use itertools for permutations and divmod function
* Day 3:  Part 1 cleverly used insight into wrapped squares, part 2 brute forced arrays
* Day 4:  More itertools to find matches of words in a passphrase, part 1 unsorted part 2 sorted
* Day 5:  Simple rules to move up and down a stack
* Day 6:  "Reallocate" values by looping, looking for previous states.  I stored and recognized previous states by combining into strings.  Part 2 was effectively solved, which maybe means there is a clever solution for Part 1 that didn't require the whole thing.
* Day 7:  Create tree given specification of node name + children names.  Used classes, and _dictionary comprehensions_.
* Day 8:  Iteration over rules to increment registers.  Dictionaries.
* Day 9:  Iterate through long string to remove "garbage" and count group depths
* Day 10:  Creating a hash algorithm, based upon reversing sections of a ring-array.  Interesting, if maddening in its details.
* Day 11:  Follow instructions to walk along a hex grid.  Fun!  Red Blob Games blog posting was _very helpful_:  https://www.redblobgames.com/grids/hexagons/
* Day 12:  Iteratively walk a graph to identify the number of connected nodes.  Also an interesting use of dictionary comprehension + regex for input.
* Day 13:  Mod to find location of "scanners".  This took longer than necessary, because of a misinterpretation of part 2 (not severity=0 but rather any hit).  I think that there is a much much faster solution if one looks at the times allowable by the particular scanner layers.
* Day 14:  Use the knot hash from day 10 to create a 128x128 grid from a base key+number in binary.  Part two required finding contiguous elements, used some recursion to identify and remove "seen" elements.
* Day 15:  Compare the lowest 16-bits of the results of two generator functions, i.e. bit and with 65535.  Completed this within 50 mins of the start, but was still ~800 or so.
* Day 16:  Follow the instructions to iterate a string, very usual.  For part 2 the key insight is that there is a limit cycle, as brute-forcing a billion iterations is not feasible on current hardware.
* Day 17:  Here's a case where brute force (50M iterations) are feasible, but only if the individual operations are fast enough.  After failing with a regular list, a deque seems to work better.
* Day 18:  More instructions + state tracking.  Dictionaries are helpful.  Part 2 took time to debug, because I hadn't been removing from the front of the list.
* Day 19:  Follow a line in a big string array "map".  The trickiest part is setting up direction arrays.
* Day 20:  Simulate particle given initial position, velocity, acceleration.  Part 2 involved looking for collisions.  I tried math (computing potential collision times between each particle using quadratic equation, but that ended up being too complex.  Just brute force it.
* Day 21:  *SKIPPED*
* Day 22:  Walking around a big ("infinite") grid, changing states.  I used string manipulation, which was probably slower than necessary.




## See previous work at:
* https://github.com/jborlik/AdventOfCode2015
* https://github.com/jborlik/AdventOfCode2016