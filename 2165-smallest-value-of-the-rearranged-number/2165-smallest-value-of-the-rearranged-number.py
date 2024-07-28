class Solution:
    def smallestNumber(self, num: int) -> int:

        if num == 0:
            return 0
        elif num > 0:
            l = list(str(num))
            l.sort()
            i = 0
            while i < len(l):
                if l[i] == "0":
                    i += 1
                else:
                    break
            return int(l[i] + ("").join(l[:i] + l[i + 1 :]))
        else:
            l = list(str(num))
            a = l[1:]
            a.sort(reverse=True)
            return int("-" + ("").join(a))
