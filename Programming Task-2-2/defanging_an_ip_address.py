class Solution:
    def defangIPaddr(self, a: str) -> str:
        a = a.replace('.',"[.]")
        return a
