'''

Description:

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        ascii_sum_of_s = sum( map( lambda x: ord(x), s) )
        ascii_sum_of_t = sum( map( lambda x: ord(x), t) )
        
        adding_char = chr( ascii_sum_of_t - ascii_sum_of_s )
        
        return adding_char


# N : the number of string t

## Time Complexity: O( N )
#
# It seems to be O( 1 ) at first glimpse, but it takes O( N ) actually.
# The hidden overhead is the summation of ascii code for every charachter in s and t.

## Space Complexity: O( 1 )
#
# The overhead in space is variables for the ascii sum and difference of them.


def test_bench():

    test_data = [
                    ("abcd", "abcde"),
                    ("abcd", "aabcd"),
                    ("abcd", "abccd")
                ]

    # expected output:
    '''
    e
    a
    c
    '''

    for s, t in test_data:

        print( Solution().findTheDifference(s, t) )

    return



if __name__ == '__main__':

    test_bench()