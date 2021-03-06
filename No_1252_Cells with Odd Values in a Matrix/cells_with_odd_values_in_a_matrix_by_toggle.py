'''

Description:


Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.



Example 1:

Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.



Example 2:

Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
 


Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m

'''




# Note: 
# odd value element must be added with 1 by 2k+1 times = toggle 2k+1 times
# where k = 0, 1, 2, 3, ...

from typing import List
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        
        rows, cols = n, m
        
        rows_flag, cols_flag = [0]*rows, [0]*cols
        
        for operations in indices:
            
            row_index, col_index = operations
            
            # toggle {0,1} for specified row
            rows_flag[row_index] ^= 1
        
            # toggle {0,1} for specified column
            cols_flag[col_index] ^= 1
            
        
        

        # collect odd number elements
        number_of_odds = 0
        
        for i in range(cols):
            for j in range(rows):
                number_of_odds += rows_flag[j]^cols_flag[i]
        
        
        return number_of_odds



# n, m : the dimension of rows and columns
# L : the length of operation sequence

## Time Complexity: O( m * n + L )
#
# The overhead in time is the for loop iterating on operations, which is of O( L ),
# and the loop iterating on (i, j), which is of O( m * n )
# It takes O( m*n ) in total.


## Space Complexity: O( m + n )
#
# The overhead in space is the storage for rows_flag as well as cols_flag, which si of O( m + n ).



def test_bench():

    test_data = [
                    (2, 3, ([[0,1],[1,1]]) ),
                    (2, 2, ([[1,1],[0,0]]) )
                ]

    for n, m , indices in test_data:

        print( Solution().oddCells(n, m, indices) )
    
    return 



if __name__ == '__main__':

    test_bench()