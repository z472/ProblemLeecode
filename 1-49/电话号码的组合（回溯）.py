class Solution:
    def letterCombinations(self, digits):     # digits: str -> List[str]
        if digits == '':
            return []
        adict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        l = len(digits)
        output = []
        if l > 1:
            for i in adict[digits[0]]:
                for j in self.letterCombinations(digits[1:]):
                    output.append(i+j)
        else:
            for i in adict[digits[0]]:
                output.append(i)
        return output

a = Solution()
test = ['232', ]
for i in test:
    print(a.letterCombinations(i))
