'''

Description:

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        # root node of binary search tree
        root = TreeNode( preorder[0] )
        
        bst_stack = [ root ]
        
        for node_value in preorder[1:]:
            
            
            if node_value < bst_stack[-1].val:
                # build left child node    
                bst_stack[-1].left = TreeNode( node_value )
                bst_stack.append( bst_stack[-1].left )
            
            else:
                # build right child node
                while bst_stack and bst_stack[-1].val < node_value:
                    branch_node = bst_stack.pop()
                
                branch_node.right = TreeNode( node_value )
                bst_stack.append( branch_node.right )
                
        return root



# n : the length of preorder sequence, 

## Time Complexity: O( n )
#
# The overhead in time is the cost of pre-order DFS traversal, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for new binary tree, which is of O( n )



def inorder_print( node: TreeNode):

    if node:

        inorder_print( node.left )
        print( f'{node.val} ', end = ' ')
        inorder_print( node.right )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'pre_order_sequence')
def test_bench():

    test_data = [ 
                    TestEntry( pre_order_sequence = [8,5,1,7,10,12] ),
                    TestEntry( pre_order_sequence = [5,3,2,4,7,6,8] ),
                ]

    # expected output:
    '''
    1  5  7  8  10  12  
    2  3  4  5  6  7  8
    '''

    for t in test_data:

        root = Solution().bstFromPreorder( preorder = t.pre_order_sequence )

        inorder_print( root )
        print()

    return



if __name__ == '__main__':

    test_bench()