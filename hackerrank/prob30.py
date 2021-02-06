def split_and_join(line):
    # write your code here
    values=""
    for j in line:
        if(j==" "):
            values=values+"-"
        else:
            values=values+j
    return values
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
