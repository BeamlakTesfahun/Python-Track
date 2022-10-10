class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = Counter(changed)
        #if odd return an empty list
        if c[0]%2:
            return []
        for y in sorted(c):
            if c[y] > c[2*y]:
                return []
            c[2*y] -= c[y] if y else c[y]//2
        return list(c.elements())
