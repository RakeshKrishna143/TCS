def find_Novowel(a):
    b= 'aeiou'
    c = []
    for i in a:
        j = i.lower()
        if len(set(i)&set(b))==0:
            c.append(i)
    return c
            

if __name__ == '__main__':
    c = int(input())
    a= []
    for i in range(c):
        a.append(input())
    output = find_Novowel(a)
    if len(output)==0:
        print('No element without vowel is present')
    else:
        for i in output:
            print(i)
