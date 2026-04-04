import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("time:",end - start)
    return wrapper
@timer
def tasks():
    for i in range(1000000):
        pass
tasks()
