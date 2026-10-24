class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        month_days = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}

        aA_date = int(arriveAlice[3:])
        lA_date = int(leaveAlice[3:])
        aB_date = int(arriveBob[3:])
        lB_date = int(leaveBob[3:])

        aA_month = int(arriveAlice[:2])
        lA_month = int(leaveAlice[:2])
        aB_month = int(arriveBob[:2])
        lB_month = int(leaveBob[:2])

        A_Aday = month_days[aA_month] + aA_date
        A_lday = month_days[lA_month] + lA_date
        B_Aday = month_days[aB_month] + aB_date
        B_lday = month_days[lB_month] + lB_date

        min_date = 0
        max_date = 0

        if A_lday > B_lday:
            max_date = B_lday
        else:
            max_date = A_lday
        
        if A_Aday > B_Aday:
            min_date = A_Aday
        else:
            min_date = B_Aday
        
        ans = (max_date - min_date) + 1

        if ans < 0:
            return 0
        else:
            return ans 

