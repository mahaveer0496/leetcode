'''

Description:

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note: There are at least two nodes in this BST.

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        
        #min_diff = 2**31
        prev_node_value = -2**31
        
        def helper( node: TreeNode):
            
            if node:
                
                yield from helper( node.left )
                
    
                nonlocal prev_node_value
                
                yield (node.val - prev_node_value)
                
                prev_node_value = node.val
                                
                yield from helper( node.right )
                
        return min( helper( root ) )



# n : the number of nodes in binary search tree

## Time Complexity: O( n )
#
# The overhead in time is the cost of in-order traversal, which is of O( n )

## Space Complexity: O( n )
#
# THe overhead in space is the storage for recursion call stack, which is of O( n )


def test_bench():

    ## Test case_#1
    root_1 = TreeNode(1)
    root_1.right = TreeNode(3)
    root_1.right.left = TreeNode(2)

    # expected output:
    '''
    1
    '''
    print( Solution().getMinimumDifference(root_1) )



    ## Test case_#2
    root_2 = TreeNode(5)

    root_2.left = TreeNode(1)
    root_2.right = TreeNode(10)

    root_2.right.left = TreeNode(8)
    root_2.right.right = TreeNode(13)

    # expected output:
    '''
    2
    '''
    print( Solution().getMinimumDifference(root_2) )

if __name__ == '__main__':

    test_bench()