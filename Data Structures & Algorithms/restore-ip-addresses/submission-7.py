class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if len(s) > 12:
            return result

        def backtrack(i, dots, ip): #i is index we are at in string, dots
            if dots == 4 and i == len(s): #case 1: 4 dots have been used, dots have been ended
                result.append(ip[:-1])
                return
            if dots > 4:
                return

            for j in range(i, min(i+3, len(s))): #min of i+3 vs length of ip (out of bounds check)
                if i != j and s[i] == "0":
                    continue
                if int(s[i: j + 1]) < 256:
                    backtrack(j + 1, dots + 1, ip + s[i : j + 1] + ".")
        
        backtrack(0, 0, "")
        return result
