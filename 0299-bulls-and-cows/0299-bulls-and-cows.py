class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
       
        b = 0  
        c = 0  
        secret_list = list(secret)
        guess_list = list(guess)
        for i in range(len(guess)):
            if guess_list[i] == secret_list[i]:
                b += 1
                secret_list[i] = '*'
                guess_list[i] = '*'

        for i in range(len(guess)):
            if guess_list[i] != '*' and guess_list[i] in secret_list:
                c += 1
                secret_list[secret_list.index(guess_list[i])] = '*'

        return str(b)+"A"+str(c)+"B"

