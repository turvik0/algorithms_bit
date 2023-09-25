class Solution(object):
    def isValid(self, s):
        charactars = []
        for i in s:
            if i =='(' or i=='[' or i=='{':
                charactars.append(i)
            else:
                if (i == ')' and charactars[-1] != '(') or (i == '}' and charactars[-1] != '{') or (i == ']' and charactars[-1] != '['):
                    return False
                charactars.pop()
        return not charactars