class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3:
            month += 12
            year -= 1

        q = day 
        m = month 
        k = year%100
        j = year//100 
        days = ["Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        h = (q + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * j) % 7
        return days[h]
        
        