def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    newInt = 0
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    i = 0
    while i < len(s):
        value = 0
        print(s[i])
    

        if i < (len(s) - 1) and s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
            i = i + 1
            value = dict.get(s[i]) - 1
        elif i < (len(s) - 1) and s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
            i = i + 1
            value = dict.get(s[i]) - 10
        elif i < (len(s) - 1) and s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
            i = i + 1
            value = dict.get(s[i]) - 100
        else:
            value = dict.get(s[i])

        newInt = newInt + value
        
        print(newInt)
        i = i + 1



romanToInt("III")
