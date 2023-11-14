"""

    mini-task2.py

    Determine which counting technique performs best by using the timeit module.

"""
from statistics import mean
import timeit

from most_common import most_common_technique1, most_common_technique2, most_common_technique3, most_common_technique4

# If there's a problem importing, try one of the other two shown here...
# from ch02_automation.most_common import most_common_technique1, most_common_technique2, most_common_technique3
# from .most_common import most_common_technique1, most_common_technique2, most_common_technique3


data = [1, 2, 3, 4, 5, 3, 1, 5, 2, 1, 5, 3, 4, 2, 5]
iters = 100000

results1 = timeit.repeat('most_common_technique1(data)', number=iters, globals=globals())
results2 = timeit.repeat('most_common_technique2(data)', number=iters, globals=globals())
results3 = timeit.repeat('most_common_technique3(data)', number=iters, globals=globals())
results4 = timeit.repeat('most_common_technique4(data)', number=iters, globals=globals())

print(mean(results1), mean(results2), mean(results3), mean(results4))
