class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        charFound=False
        for l in s[::-1]:
            if l != " " and charFound == False:
                charFound = True
            if l != " " and charFound == True:
                count+=1
            if l== " " and charFound == True:
                break

        return count

solObj = Solution()

s = "   fly me   to   the moon  "
print(solObj.lengthOfLastWord(s))