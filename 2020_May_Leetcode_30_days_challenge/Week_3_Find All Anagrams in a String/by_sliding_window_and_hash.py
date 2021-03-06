'''

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.



Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".



Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''



from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def helper( s: str, p: str):
            signature, size_p = sum( map(hash,p) ), len(p)
            size_s = len(s)

            if size_s * size_p == 0 or size_p > size_s :
                # Quick response:
                # Reject empty string
                # Reject oversize pattern
                return []

            cur_signature = sum( map( hash, (s[:size_p]) ) )

            for tail_of_window in range( size_p, size_s ):

                head_of_window = tail_of_window - size_p

                if cur_signature == signature:
                    yield head_of_window

                new_char, old_char = s[tail_of_window], s[ head_of_window ]

                cur_signature += ( hash(new_char) - hash(old_char) )

            # handle for last iteration    
            if cur_signature == signature:
                yield ( size_s - size_p )
        
        # -----------------------
        return [ *helper(s, p) ]



# n : the character length of input s

## Time Complexity: O( n  )
#
# The overhead in time is the for loop, iterating on s, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 's p')
def test_bench():

    test_data = [
                    TestEntry( s = "cbaebabacd", p = "abc"),
                    TestEntry( s = "abab", p = "ab"),
                    TestEntry( s = "", p = "ab"),
                    TestEntry( s = "abab", p = ""),
                    TestEntry( s = "abab", p = "ababababab"),
                ]


    # expected output:
    '''
    [0, 6]
    [0, 1, 2]
    []
    []
    []    
    '''

    for t in test_data:

        print( Solution().findAnagrams( *t ) )
    
    return 



if __name__ == '__main__':

    test_bench()