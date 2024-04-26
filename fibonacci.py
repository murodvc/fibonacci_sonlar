class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current += 1
        return result

def main():
    n = int(input("Fibonacci ketma-ketligining nechinchi elementigacha n = "))
    fibonacci_iter = FibonacciIterator(n)
    for fib_num in fibonacci_iter:
        print(fib_num, end=" ")

if __name__ == "__main__":
    main()