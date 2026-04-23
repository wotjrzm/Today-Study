import sys

def solve():
    n = int(sys.stdin.readline())
    ant_den = {}

    for _ in range(n):
        data = sys.stdin.readline().split()
        k = int(data[0])
        foods = data[1:]
        
        current = ant_den
        for food in foods:
            # 해당 먹이가 현재 층에 없으면 새로 생성
            if food not in current:
                current[food] = {}
            # 다음 층으로 이동
            current = current[food]

            
    def print_ant_den(current_dict, depth):
        # 정렬
        sorted_foods = sorted(current_dict.keys())
        
        for food in sorted_foods:
            print("--" * depth + food)
            print_ant_den(current_dict[food], depth + 1)

    # 출력
    print_ant_den(ant_den, 0)

if __name__ == "__main__":
    solve()