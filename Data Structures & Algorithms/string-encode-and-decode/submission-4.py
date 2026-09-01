class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""#"<,"
        for word in strs:
            if word == "":
                res+= "~^~/empty"
            else:
                res += "~^~" + word

        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "":
            return []
        s = s[3:]
        res = s.split("~^~")
        for i in range(len(res)):
            if res[i] == "/empty":
                res[i] = ""
        return res
