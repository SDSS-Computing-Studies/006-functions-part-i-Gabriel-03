#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
def largest(List):
    List.sort()
    a=List[-1]
    return a
print(largest([3,1,4,7,13,6]))
print(largest([5,1,9]))
