class Solution:
    def minOperations(self, logs: List[str]) -> int:
        num_operations = 0

        for log in logs:
            if log == '../':
                if num_operations > 0:
                    num_operations -= 1
            elif log == './':
                continue
            else:
                num_operations += 1

        return num_operations
