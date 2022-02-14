class Solution:
    def countAndSay(self, n):      # n: int   return: -> str
        if n == 1:
            return '1'
        output, prestr = '', self.countAndSay(n-1)
        amount, snumber = 0, prestr[0]
        for i in prestr:
            if i == snumber:
                amount += 1
            else:
                output += str(amount)+snumber
                amount, snumber = 1, i
        output += str(amount) + snumber
        return output

