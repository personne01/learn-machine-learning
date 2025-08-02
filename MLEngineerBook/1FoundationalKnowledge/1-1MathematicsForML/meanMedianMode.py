
import numpy
from scipy import stats


nilai = [99,86,87,88,88,86,89,87,94,78,77,85,86]

"""
    ===== 1. MEAN =====
    - The Average Value
    - manually to calculate this is sum of all these value and devide the sum by the number of values (sumNilai/countNilai)
"""
meanNilai = numpy.mean(nilai)
print(meanNilai)

"""
    ===== 2. MEDIAN =====
    - The Mid Point Value
    - 
"""
medianNilai = numpy.median(nilai)
print(medianNilai)

"""
    ===== 3. MODE =====
    The most common value
"""
modeNilai = stats.mode(nilai)
print(modeNilai)


