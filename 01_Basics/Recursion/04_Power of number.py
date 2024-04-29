'''
2^5 ; 2*2*2*2*2 (2,5) = 32

'''

def power(n,p):
    if p==0:
        return 1
    return n * power(n,p-1)

print(power(2,5))