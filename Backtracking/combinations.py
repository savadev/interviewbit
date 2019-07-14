'''
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        def fillCombinations(n, index, k, curr, combinations):
            if k <= 0:
                combinations.append(list(curr))
                return
            if k > n - index + 1:
                return
            fillCombinations(n, index + 1, k, curr, combinations)
            curr.append(index)
            fillCombinations(n, index + 1, k - 1, curr, combinations)
            curr.pop()

        combinations = []
        fillCombinations(A, 1, B, [], combinations)
        return sorted(combinations)
