def split_and_join(line):
    # write your code here
    #print(line, type(line))
    res = ""
    for i in range(0,len(line)):
        if (line[i] == " "):
            ch = "-"
            res += ch
        else:
            res += line[i]
    #print(res)
    return(res)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
