class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = collections.Counter(t)
        if not (collections.Counter(s) >= t_dict):
            return ""
        required, soln,formed = deque(),(0,len(s)),0
        curr_window_freq = collections.Counter()
        for i, char in enumerate(s):
            if char in t_dict:
                curr_window_freq[char] += 1
                if curr_window_freq[char] == t_dict[char]:
                    formed += 1
                required.append(i)
                #determine if we can move left more to the next settle point
                while curr_window_freq[s[required[0]]] > t_dict[s[required[0]]]:
                    index_removed = required.popleft()
                    curr_window_freq[s[index_removed]] -= 1
                #compare and store Solution
                if soln[1] - soln[0] > i - required[0]+1 and formed == len(t_dict):
                    soln = (required[0], i+1)

        return s[soln[0]:soln[1]]