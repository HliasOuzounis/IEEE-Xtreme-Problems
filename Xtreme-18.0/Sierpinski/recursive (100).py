import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()

BLUE = 0
RED = 1

def find_color(x, y, height):
    if height == 2:
        return RED
    
    if y > height // 2:
        return find_color(x, y - height // 2 - 1, height // 2)
    
    if x + y < height // 2 + 1:
        return find_color(x, y, height // 2)
    
    if x <= height // 2 + 1:
        return BLUE
    else:
        return find_color(x - height // 2 - 1, y, height // 2)


def solve_case():
    y, x = get_numbers()
    
    height = 2
    while height < y:
        height *= 2
        height += 1
        
    y = height - y
    
    print(find_color(x, y, height))
    

def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
