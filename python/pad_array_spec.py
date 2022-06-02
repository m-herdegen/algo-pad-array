# Write unit tests!
from pad_array import pad
print(pad([1,2,3], 5) == [1,2,3,None,None])

print(pad([1,2,3], 5, 'apple') == [1,2,3,'apple', 'apple'])
