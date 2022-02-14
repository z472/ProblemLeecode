class Solution:
    def intToRoman(self, num):
        romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        alb = [1, 5, 10, 50, 100, 500, 1000]
        spe_roman = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        spe_alb = [4, 9, 40, 90, 400, 900]
        output = ''
        x = lambda l: list(reversed(l))
        romans, spe_roman, spe_alb = x(romans), x(spe_roman), x(spe_alb)
        # print(romans, spe_roman, spe_alb)
        for idx, i in enumerate(reversed(alb)):
            add = num // i
            output += romans[idx]*add
            remainder = num % i
            if alb[6-idx] != 1 and remainder // spe_alb[idx] == 1:
                output += spe_roman[idx]
                remainder -= spe_alb[idx]
            num = remainder
        return output

a = Solution()
test = [3, 4, 9, 58, 1994]
for i in test:
    print(a.intToRoman(i))
# print(a.intToRoman(1994))
