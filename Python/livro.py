from functools import partial
from operator import mul

def create_multipliers():
    return [partial(mul, i) for i in range(5)]

multipliers = create_multipliers()
print([multiplier(5) for multiplier in multipliers])  # Saída: [0, 5, 10, 15, 20]
