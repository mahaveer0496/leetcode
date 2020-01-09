'''

Description:

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

'''



from typing import List
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        size = len(A)
        
        sorted_array = [0]*size
        even_index, odd_index = 0, 1
        
        for x in A:
            
            if x & 1:
                sorted_array[odd_index] = x
                odd_index += 2
            else:
                sorted_array[even_index] = x
                even_index += 2
                
        return sorted_array
                


# n : the length of input list, A.

## Time Complexity: O( n )
# 
# The overhead in time is the for loop iterating on x, which is of O( n ).

## Space Complexity: O( n )
# 
# The overhead in space is the storage for sorted_array, which is of O( n ). 



def test_bench():

    test_data = [
                    [4,2,5,7],
                    [1,3,5,7,9,2,4,6,8,10]
                ]

    # expected output:
    '''
    [4, 5, 2, 7]
    [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
    '''


    for sequence in test_data :

        print( Solution().sortArrayByParityII( sequence) )

    return 



if __name__ == '__main__':
    test_bench()