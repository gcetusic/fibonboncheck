#! /usr/bin/python

class Fibonacci:
    """Compute Fibonacci series using Dijkstra's clever algorithm
    
    The n parameter must be integers (hex or otherwise) or the program will fail

    >>> fibnum = Fibonacci()
    >>> fibnum.fib(123)
    22698374052006863956975682L

    >>> fibnum = Fibonacci()
    >>> fibnum.fib(0x23)
    9227465

    """ 
    fibs = {0: 0, 1: 1}
    def fib(self, n):
        
        if n in self.fibs: return self.fibs[n]
        if n % 2 == 0:
            self.fibs[n] = ((2 * self.fib((n / 2) - 1)) + self.fib(n / 2)) * self.fib(n / 2)
            return self.fibs[n]
        else:
            self.fibs[n] = (self.fib((n - 1) / 2) ** 2) + (self.fib((n+1) / 2) ** 2)
            return self.fibs[n]

def main():
    if not len(sys.argv)==2:
        help = sys.argv[0] + " fibnumber"
        print "Error: script needs exactly one argument\n" + help
        sys.exit(-1)
    fibnum = Fibonacci()
    try:
        n = int(sys.argv[1])
    except:
        print "Error parsing arguments, probably not integers"
        sys.exit(-2)

    print fibnum.fib(n)

if __name__ == "__main__":
    import sys
    main()
    