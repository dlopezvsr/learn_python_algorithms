class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = ""
        operator = ["-", "+"]
        left = 0
        s = s.strip()

        if len(s) <= 0:
            return 0

        for char in s:
            if not char.isdigit() and left == 0:
                if char in operator:
                    if len(s) < 2:
                        return 0
                    number = number + char
                    left += 1
                else:
                    return 0
            elif not char.isdigit():
                if left == 1 and not number.isdigit():
                    return 0
                else:
                    break
            else:
                number = number + char
                left += 1

        number = int(number)

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if number > INT_MAX:
            number = INT_MAX
        if number < INT_MIN:
            number = INT_MIN

        return number