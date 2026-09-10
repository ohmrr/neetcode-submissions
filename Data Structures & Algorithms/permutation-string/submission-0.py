class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = defaultdict(int), defaultdict(int)

        for c in s1:
            s1_count[c] += 1

        for right in range(len(s2)):
            left = right - len(s1) + 1

            if left < 0:
                continue

            for c in s2[left:right + 1]:
                s2_count[c] += 1

            if s2_count == s1_count: return True
            else:
                s2_count.clear()



        return False