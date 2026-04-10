def solve(a, b, c):
    
    if b == 1:
        return a % c
    
    half = solve(a, b // 2, c)
    temp = (half * half) % c
    
    if b % 2 == 0:
        return temp % c
    
    else:
        return (temp * a) % c

a, b, c = map(int, input().split())   
print(solve(a,b,c))