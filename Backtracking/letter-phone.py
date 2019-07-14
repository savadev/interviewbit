'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

![Image](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
'''


class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        def fillResults(A, index, result, genResult, mapping):
            if index >= len(A):
                result.append(''.join(genResult))
                return
            s = mapping[int(A[index])]
            for c in s:
                genResult.append(c)
                fillResults(A, index + 1, result, genResult, mapping)
                genResult.pop()

        mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        genResult = []
        fillResults(A, 0, result, genResult, mapping)
        return result
