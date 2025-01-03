# TODO implement better solution

def sol1(nums) -> list:
    digitLog = []
    letterLogMap = {}
    tmpStr = ""
    duplicateKeys = []
    res = []
    for n in nums:
        if isDigit(n):
            digitLog.append(n)
        else:
            if " ".join(n.split(" ")[1:]) in duplicateKeys:
                letterLogMap[" ".join(n.split(" ")[1:]) + " " + n.split(" ")[0]] = n
            
            elif " ".join(n.split(" ")[1:]) in letterLogMap:
                duplicateKeys.append(" ".join(n.split(" ")[1:]))
                letterLogMap[" ".join(n.split(" ")[1:]) + " " + n.split(" ")[0]] = n
                tmpStr = letterLogMap.pop(" ".join(n.split(" ")[1:]))
                letterLogMap[
                    " ".join(tmpStr.split(" ")[1:]) + " " + tmpStr.split(" ")[0]
                ] = tmpStr

            else:
                letterLogMap[" ".join(n.split(" ")[1:])] = n

    letterLogKeys = sorted(list(letterLogMap.keys()))
    print(letterLogMap)
    for k in letterLogKeys:
        res.append(letterLogMap.get(k))

    res.extend(digitLog)
    return res


def isDigit(str) -> bool:
    flag = True
    for s in str.split(" ")[1:]:
        if not s.isnumeric():
            flag = False

    return flag


nums = ["zoey i love you", "lucas i love you", "rong i love you"]

print(nums)
print(sol1(nums))
