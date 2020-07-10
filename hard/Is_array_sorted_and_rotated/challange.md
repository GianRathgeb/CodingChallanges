# Check if an array is sorted and rotated

Given an array of `N` distinct integers. The task is to write a program to check if this array is sorted and rotated `clockwise`. If the array is sorted and rotated then return `Yes` otherwise return `NO`

## Examples

```

def check([3, 4, 5, 1, 2]) ➞ "YES"
The above array is sorted and rotated.
Sorted array: [1, 2, 3, 4, 5]. 
Rotating this sorted array clockwise 
by 3 positions, we get: [3, 4, 5, 1, 2]

def check([1, 2, 3]) ➞ "NO"
The above array is sorted but not rotated.

def check([7, 9, 11, 12, 5]) ➞ "YES"
The above array is sorted and rotated.
Sorted array: [5, 7, 9, 11, 12]
Rotating this sorted array clockwise
by 4 positions, we get: [7, 9, 11, 12, 5]

```

### Notes:

N/A