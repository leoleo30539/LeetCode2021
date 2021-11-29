class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for ch_s, ch_t in zip(s, t):
            if ch_s not in dict_s:
                dict_s[ch_s] = 1
            else:
                dict_s[ch_s] += 1
            if ch_t not in dict_t:
                dict_t[ch_t] = 1
            else:
                dict_t[ch_t] += 1
        for d_s in dict_s:
            if d_s not in dict_t:
                return False
            if dict_s[d_s] != dict_t[d_s]:
                return False
        return True
        
