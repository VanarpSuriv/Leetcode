class Solution(object):
    def calPoints(self, operations):
        z = []
        for y in operations:
            if y == "+":
                z.append(z[-1] + z[-2])
            elif y == "D":
                z.append(2 * z[-1])
            elif y == "C":
                z.pop()
            else:
                z.append(int(y))
        return sum(z)