def login_required(func):
    def wrapper():
        print("checking login...")
        return func()
    return wrapper
@login_required
def dashboard():
    print("welcome to dashboard")
dashboard()
