class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local = email[:email.find('@')].replace('.', '')
            domain = email[email.find('@') + 1:]
            
            if local.find('+') != -1:
                local = local[:local.find('+')]
                
            unique.add(f'{local}@{domain}')

        return len(unique)