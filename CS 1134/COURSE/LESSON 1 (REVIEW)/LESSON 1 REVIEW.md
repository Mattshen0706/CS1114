# DIFFERENT DATA TYPES:

## STRINGS: (IMUTABLE)

"THIS IS A STRING"
'THIS IS A STRING'
"""THIS IS A STRING"""

## LISTS: (MUTABLE)

[THIS IS A LIST]

## TUPLE: (IMUTABLE)

(THIS IS A TUPLE)

## DICTIONARIES: (MUTABLE)

{THIS IS: A DICTIONARY}
{KEY:VALUE}

## LIST MEMORY MODEL: (HOMEWORK: DRAW OUT THE MEMORY MODEL)

list1=[1,2,3]


- ALIASING (REASSIGNING A LIST TO A NEW VARIABLE) (ONLY 1 LIST EXISTS IN THE MEMORY MODEL):

list2=list1

- USING COPY (CREATING A COPY WILL MAKE A 2 COPIIES OF THE LIST IN THE MEMORY MODEL):

import copy
list2=list1.copy()

- DEEPCOPY vs SHALLLOWCOPY
    - Deepcopy duplicates a list completely and takes up double the amount of space in the memory
    

# LIST METHODS:

- EXTEND (CREATES MULTIPLE ELEMENTS AT THE END OF A LIST) (DOES NOT CREATE A NEW LIST, EXTENDS ADDS TO THE ORIGINAL LIST IN PLACE)
- APPEND (ADDS ONE ELEMENT TO THE END OF A LIST) (DOES NOT CREATE A NEW LIST, ADDS TO EXISTING LIST)
- POP (TAKES OUT BASED ON INDEX) (DOES NOT CREATE A NEW LIST)
- REMOVE (TAKES OUT BASED ON VALUE) (DOES NOT CREATE A NEW LIST, ADDS TO EXISTING LIST)
- +, - and * constructs a new list 


# You will not have an index error if you create a list slicing with index out of range 


# FUNCTIONS:
- Initiated using def functionname():
- Variables declared inside the function does not affect the outside
- If you don't have a return in a function, return type will default to "NONE" and value type "NONE"

# CLASSES:


