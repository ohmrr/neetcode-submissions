class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_seniors = 0

        for ticket in details:
            age = int(ticket[11:13])

            if age > 60:
                num_seniors += 1

        return num_seniors
