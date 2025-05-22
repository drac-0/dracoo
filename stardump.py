#square
for i in range(5):
    for x in range(5) :
        print("* ",end="")
    print()

print("\n")

#normal triangle
def normal(n): 
    for i in range(n+1) :
        for x in range(i):
            print("*", end = "")
        print()

print(normal(7))

#v1 reversed
def reversed(n) :
    for i in range(n+1) :
        print("*"*(n-i))
        for x in range(i) :
            print("", end='')
    
print(reversed(7))

#v2 reversed
def reversed(n) :
    for i in range(n+1) :
        for j in range(n-i) :
            print("*",end='')
        for x in range(i) :
            print("", end='')
        print()
    
print(reversed(7))

#v3 reversed
def reversed(n) :
    for i in range(n+1) :
        for j in range(n-i) :
            print("*", end='')
        print()
    
print(reversed(7))

#v4 reversed
def reversed(n) :
    for i in range(n+1) :
        for j in range(1,n) :
            print("*", end='')
        print()
    
print(reversed(7))


def right_sided(n) :
    for i in range(n+1) :
        for j in range(i,n) :
            print(" ", end='')
        for r in range(i) :
            print("*", end='')
        print()
    
print(right_sided(7))

def right_sided_reversed(n) :
    for i in range(n + 1) :
        for j in range(i) :
            print(" ", end="")
        for r in range(n-i):
            print("*", end='')
        print()

print(right_sided_reversed(7))

def right_sided_reversed(n) :
    for i in range(n + 1) :
        for j in range(n - i) :
            print(" ", end="")
        for r in range(i):
            print("*", end='')
        
        print()
print(right_sided_reversed(7))

def pyramid_shit(n):
    for i in range(n + 1) :
        for j in range(i,n) : #i,n can be written by (n - i)
            print (" ", end='')
        for k in range(i) :
            print("*",end='') 
        for l in range(i-1) :
            print("*", end='')
        print()

print(pyramid_shit(7))

def reversed_pyramid_shit(n) :
    for i in range(n+1) :
        for x in range(i):
            print(" ", end='')
        for j in range(i,n) :
            print("*", end='')
        for k in range((i-1),n) :
            print("*", end='')
            
        print()

print(reversed_pyramid_shit(7))


def sandclock (n) :
    n+=1
    for y in range(n-1) :
        if y != n : 
            for z in range(y+1):
                print(" ",end='')
            for x in range(n-y) :
                print("*",end='')
            
            for w in range(n-(y+1)) :
                print("*",end='')
        else:
            break
        print()
    for i in range(n) :
        for h in range(i,n):
            print(" ",end='')
        for j in range(i):
            print("*",end='')

        for k in range(i+1) :
            print("*",end='')
            
        print()
print(sandclock(7))
def diamond(n):
    for i in range(n) :
        for z in range(i,n) :
            print(" ",end='')
        for y in range(i):
            print("*",end='')
        for w in range(i-1) :
            print("*",end='')
        print()   

    for y in range(n):
        for z in range(y):
                print(" ",end='')
        for x in range(n-y) :
                print("*",end='')
        for w in range(n-(y+1)) :
                print("*",end='')

        print()

print(diamond(7))


