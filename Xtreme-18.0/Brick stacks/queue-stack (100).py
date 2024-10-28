import sys


input = lambda: sys.stdin.readline().rstrip()


def get_number():
    return int(input())


def get_numbers():
    return list(map(int, input().split()))


def get_word():
    return input()


def solve_case():
    from collections import deque
    
    n, x = get_numbers()
    bricks = get_numbers()

    bricks.sort()

    queue = deque([[bricks.pop()]])
    
    while bricks:
        next_brick = bricks.pop()
        stack = queue.popleft()
        if stack[-1] - next_brick >= x:
            stack.append(next_brick)
            queue.append(stack)
        else:
            queue.appendleft(stack)
            queue.append([next_brick])
    
    print(len(queue))
    for stack in queue:
        print(len(stack), *stack)
        

def main():
    for test_case in range(total_cases := 1):
        solve_case()


if __name__ == "__main__":
    main()
