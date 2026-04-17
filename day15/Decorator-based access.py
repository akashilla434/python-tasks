dic={
    "suraj":"developer",
    "akash":"Police"
}
def access_control(role):
    def decorator(func):
        def wrapper(name):
            if dic.get(name)==role:
                print("Accessed")
                return func(name)
            else:
                print("Denied")
        return wrapper
    return decorator
@access_control("developer")
def developer(name):
    print(f"{name} is a developer")
@access_control("Police")
def Police(name):
    print(f"{name} is a police")
@access_control("Hacker")
def Hacker(name):
    print(f"{name} is a Hacker")
developer("suraj")
Police("akash")
Hacker("ankit")
Hacker("Name")
