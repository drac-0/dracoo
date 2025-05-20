from time import sleep

a = "hello world"
c = []
for i in range(len(a)) :
    if ord(a[i]) == 32:
        c.append(' ')

    for j in range(97,123) :
        print(''.join(c) + chr(j))
        sleep(0.04)
        if chr(j) == a[i] :
            c.append(chr(j))
            break
