class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")

        # bij dezelfde bits kan je gewoon het getal matchen
        if bits1 == bits2:
            return num1
        
        # bij meer bits moet je de hoogste bits matchen
        if bits1 > bits2:
            r = num1
            remove = bits1 - bits2
            x = 1
            while remove > 0:
                # als de bit is aangeslagen moet je em weghalen
                if r & x > 0:
                    r ^= x
                    remove -= 1
                # shift naar volgende bit
                x <<= 1
            return r
        
        # bij minder bits moet je de bits matchen + de overige bits gebruiken op de laagste bits
        if bits1 < bits2:
            r = num1
            add = bits2 - bits1
            x = 1
            while add > 0:
                # als de bit niet is aangeslagen moet je em aanslaan 
                if r & x == 0:
                    r |= x
                    add -= 1
                # daarna shiften naar de volgende bit
                x <<= 1
            return r