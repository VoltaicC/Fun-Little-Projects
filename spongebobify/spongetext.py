s1 = ''
while (s1 != 'stop'):
    s1 = input()
    s2 = ''
    i = 0
    s1.lower()
    for c in s1:
        if (i % 2 == 0):
            s2 += c.upper()
        else:
            s2 += c
        i+=1
    print (s2)
