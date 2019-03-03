def swap_case(s):
    res = ""
    for i in range(0, len(s)):
        ch = s[i]
        if (ch.islower() == True):
            ch = ch.upper()
            res += ch
        else:
            ch = ch.lower()
            res += ch
    #print(res)
    return(res)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
