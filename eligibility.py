def fib(n):
    a=0
    b=1
    c=0
    if(n>0):
       
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input())
fib(n)
