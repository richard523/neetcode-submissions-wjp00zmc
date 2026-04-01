class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        k = i = 0 #k writes compressed letter, i tracks current position

        while i < n:
            chars[k] = chars[i] #overwrite compressed letter
            k += 1 #move k pointer over

            j = i + 1 #to scan # of letters
            while j < n and chars[i] == chars[j]: #have j scan forward
                j += 1

            if j - i > 1: #if size of group > 1,
                for c in str(j - i): #convert int size into parts.
                    chars[k] = c #write digit
                    k+= 1 #if multiple digits
            i = j #move read pointer to next group of characters
        return k


