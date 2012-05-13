#! /usr/bin/python

class Fibonacci:
    
    def powLF(self, n):
        if n == 1:     return (1, 1)
        L, F = self.powLF(n//2)
        L, F = (L**2 + 5*F**2) >> 1, L*F
        if n & 1:
            return ((L + 5*F)>>1, (L + F) >>1)
        else:
            return (L, F)
            
    def fib(self, n):
        return self.powLF(n)[1]

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