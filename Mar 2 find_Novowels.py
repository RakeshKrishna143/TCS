def find_Novowels(a):
    b = 'aeiou'
    c = []
    for i in a:
        j = i.lower()
        if len(set(j)&set(b))==0:
            c.append(i)
    return c
            

if __name__ == '__main__':
    c = int(input())
    a = []
    for i in range(c):
        a.append(input())
    output = find_Novowels(a)
    if len(output)==0:
        print('No vowel is present in the list')
    else:
        for i in output:
            print(i)
