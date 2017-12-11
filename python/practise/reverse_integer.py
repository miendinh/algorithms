class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        stack = []
        positve = True
        if x < 0:
            positve = False

        for c in str(abs(x)):
            stack.append(c)

        r = []
        while len(stack) > 0:
            r += [stack.pop()]

        r = int(''.join(r))

        if r > 2**31:
            return 0

        return r if positve else -r

solution = Solution()

assert(solution.reverse(123) == 321)
assert(solution.reverse(-123) == -321)
assert(solution.reverse(120) == 21)
assert(solution.reverse(1534236469) == 0)
