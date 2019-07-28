import sys, string, math

# to find the length of longest increasing  subarray

def lenOfLongIncSubArr(arr, n):
    # 'max' to store the length of longest increasing subarray
    # 'len' to store the lengths of longest increasing subarray
    max = 1
    len = 1

    # traverse the array from the 2nd element
    for i in range(1, n):

        if (arr[i] > arr[i - 1]):
            len1 = len1 + 1
        else:
            if (max < len1):
                max = len1
            len1 = 1
    # comparing the length of the last
    # increasing subarray with 'max'
    if (max < len1):
        max = len1
    return max


# Driver program to test above

n = int(input())
L = [ int(x) for x in input().split()]
print(lenOfLongIncSubArr(L, n))
