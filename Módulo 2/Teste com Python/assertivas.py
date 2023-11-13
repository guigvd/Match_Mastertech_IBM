from types import *
# import pandas as pd
# import numpy as np
from collections.abc import Iterable

#  Igual ou não igual a
# assert 5 == 5 # Success Example
# assert 5 == 3 # Fail Example

# type() is
# assert type(5) is int # Success Example
# assert type(5) is not int # Fail Example

# is [Tipo booleano]
# true = 5 == 5
# assert true is True # Success Example
# assert true is False # Fail Example

#  in y not in [iterable]
# list = [1, 2, 3, 4, 5]
# assert 5 in list # Success Example
# assert 5 not in list # Fail Example

true_statement = 5 == 5 and 10 == 10
false_statement = 5 == 3 and 10 == 2

print(true_statement, false_statement)

assert true_statement # Success Example
assert false_statement # Fail Example