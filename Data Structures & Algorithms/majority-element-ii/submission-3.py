class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = 0, 0
        cnt1, cnt2 = 0, 0

        for n in nums:
            if num1 == n:
                cnt1 += 1
            elif num2 == n:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = n
                cnt1 = 1
            elif cnt2 == 0:
                num2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        result = []
        for n in nums:
            if n == num1:
                cnt1 += 1
            elif n == num2:
                cnt2 += 1

        if cnt1 > len(nums) // 3:
            result.append(num1)
        if cnt2 > len(nums) // 3:
            result.append(num2)

        return result
        