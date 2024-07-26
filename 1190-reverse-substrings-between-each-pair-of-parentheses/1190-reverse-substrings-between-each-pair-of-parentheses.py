class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '(' in s and ')' in s:
            open_index = s.rfind('(')
            close_index = s.find(')', open_index)
            to_reverse = s[open_index+1:close_index]
            reversed_part = to_reverse[::-1]
            s = s[:open_index] + reversed_part + s[close_index+1:]
            
        return s



        