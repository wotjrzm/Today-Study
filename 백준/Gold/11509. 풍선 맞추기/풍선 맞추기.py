import sys

def solve():
    N = int(sys.stdin.readline())
    H = list(map(int, sys.stdin.readline().split()))
    
    a = [0] * 1000001
    count = 0
    
    for h in H:
        if a[h] > 0:
            a[h] -= 1
            a[h-1] += 1
        else:
            count += 1
            a[h-1] += 1
      
    return count

if __name__ == "__main__":
    print(solve())