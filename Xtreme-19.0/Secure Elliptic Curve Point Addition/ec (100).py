# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
    
def get_numbers(n):
    return [get_number() for _ in range(n)]

def mod_inverse(k, p):
    # Fermat's little theorem for modular inverse when p is prime
    return pow(k, p - 2, p)

def solve_case():
    a, b, p, x1, y1, x2, y2 = get_numbers(7)
    # Normalize coordinates to field
    x1, y1, x2, y2 = x1 % p, y1 % p, x2 % p, y2 % p

    # Handle point at infinity cases
    if x1 == x2:
        if y1 == y2 == 0:
            print("POINT_AT_INFINITY")
            return
        elif y1 == y2:
            # Point doubling: (x3, y3) = 2*(x1, y1)
            s = ((3 * x1 * x1 + a) * mod_inverse(2 * y1, p)) % p
        else:
            # Points are inverses, result is point at infinity
            print("POINT_AT_INFINITY")
            return
    else:
        # Regular addition
        s = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p

    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p

    print(x3, y3)


def main():
    for test_case in range(total_cases := get_number()):
        solve_case()


if __name__ == "__main__":
    main()
