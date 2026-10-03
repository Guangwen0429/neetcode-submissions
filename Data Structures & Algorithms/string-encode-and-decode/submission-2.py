class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(str(len(word)) + "#" + word)

        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        result = []
        m = len(s)
        i = 0
        j = 0
        while i < m:
            if s[i] != "#":
                i += 1
                continue
            length = int(s[j:i])
            result.append(s[i+1: i+1+length])
            j = i + 1 + length
            i = i + 1 + length

        return result


