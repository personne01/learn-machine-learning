import numpy as np

"""
    ==== Percentile ====
    Percentiles are used in statistics to give you a number 
    that describes the value that a given percent of the values are lower than.
"""

age = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
p = np.percentile(age,45)
print(p)

