from numpy import *

Arr = array([1, 2, 3, 4, 5, 6, 7, 8, 9])

Max = Arr[0]

for i in range(1, len(Arr)):
    if Arr[i] > Max:
        Max = Arr[i]

print("Max Value is: ", Max)
