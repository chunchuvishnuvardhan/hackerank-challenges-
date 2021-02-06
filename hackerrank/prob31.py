def mutate_string(string, position, character):
    values=[]
    fs=''
    for j in range(0,len(string)):
        values.append(string[j])
    for k in range(0,len(values)):
        if k==position:
            values[k]=character
            fs = fs + values[k]
        else:
            fs=fs+values[k]
    return fs

if __name__ == '__main__':
    s = input('')
    i, c = input('').split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)