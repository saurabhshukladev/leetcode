from typing import List

# # Method 1
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digitLog = []
#         letterLogMap = {}

#         res = []
#         duplicateKeys = []
#         for n in logs:
#             if isDigit(n):
#                 digitLog.append(n)
#             else:
#                 if " ".join(n.split(" ")[1:]) in duplicateKeys: # fix: follow this format for all the items to reduce complexity
#                     letterLogMap[" ".join(n.split(" ")[1:]) + " " + n.split(" ")[0]] = n
                
#                 elif " ".join(n.split(" ")[1:]) in letterLogMap:
#                     duplicateKeys.append(" ".join(n.split(" ")[1:]))
#                     letterLogMap[" ".join(n.split(" ")[1:]) + " " + n.split(" ")[0]] = n
#                     tmpStr = letterLogMap.pop(" ".join(n.split(" ")[1:]))
#                     letterLogMap[
#                         " ".join(tmpStr.split(" ")[1:]) + " " + tmpStr.split(" ")[0]
#                     ] = tmpStr

#                 else:
#                     letterLogMap[" ".join(n.split(" ")[1:])] = n
        
#         letterLogKeys = sorted(list(letterLogMap.keys())) # this sort is not very good need to do sort on tuples or make sort from scratch

#         for k in letterLogKeys:
#             res.append(letterLogMap.get(k))

#         res.extend(digitLog)
#         return res


# def isDigit(str) -> bool: 
#     flag = True
#     for s in str.split(" ")[1:]: # fix: this loop doesnt need to complete, to check for digit
#         if not s.isnumeric():
#             flag = False

#     return flag

# Method 2 : source GPT modified to make it simpler
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def isDigit(log: str) -> bool:
            # Check if the content of the log (excluding the identifier) is a digit log
            return log.split(" ", 1)[1][0].isdigit()
            # return log.split(" ")[1].isdigit() # we can do this as well but then the loop to split the list runs longer than it needs to
        
        # Separate letter logs and digit logs
        letterLogs = []
        digitLogs = []
        
        for log in logs:
            if isDigit(log):
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        
        # Sort letter logs
        # Sort by content first, and then by identifier if contents are the same
        letterLogs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0])) 
        
        # Combine sorted letter logs with digit logs
        return letterLogs + digitLogs
    
# Method 3: from leetcode
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs,key = self.sort)
    def sort(self,logs):
            a,b = logs.split(' ', 1)
            if b[0].isalpha():
                return (0,b,a)
            else:
                return (1,None,None)



nums = ["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]

solObj = Solution()

print(nums)
print(solObj.reorderLogFiles(nums))
