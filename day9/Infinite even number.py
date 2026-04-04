def even_generator():
    num = 2
    while true:
        yield num
        num +=2
n=int(input("enter how many even numbers:"))
gen = even_generator()
for i in range(n):
    print(next(gen))
