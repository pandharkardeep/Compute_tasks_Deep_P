def mutate_string(string, position, character):
    count = -1
    lis = []
    for j in string:
        count+=1
        if count == position:
            j=character
        lis.append(j)
    string = ''.join(map(str, lis)) 
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)