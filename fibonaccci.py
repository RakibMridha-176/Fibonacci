from typing import Generator

def fibonacci_generator()-> Generator[int, None, None]:
    a, b= 0, 1
    while True:
        yield a
        a, b = b, (a+b)

def main()->None:
    fib_gen: Generator[int, None, None] = fibonacci_generator()
    n : int = 10
    line_break : str = ('_'*25)

    while True:
        input(f'Tap "Enter" for the next {n} number of fibonacci')

        for i in range(n):
            print(f'{next(fib_gen)}')
            print(line_break)

if __name__== '__main__':
    main()
