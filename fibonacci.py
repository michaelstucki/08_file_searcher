
def main():
    # print('via list')
    # fib = fibonacci(100)
    # for n in fib:
    #     print(n, end=', ')
    # print()

    print('via yield')
    fib = fibonacci_co()
    for n in fib:
        if n > 100000:
            break

        print(n, end=', ')
    print()


def fibonacci(limit):
    nums = []
    current = 0
    next = 1
    while current < limit:
        current, next = next, current + next
        nums.append(current)

    return nums


def fibonacci_co():
    current = 0
    next = 1
    while True:
        current, next = next, current + next
        yield current


if __name__ == '__main__':
    main()
