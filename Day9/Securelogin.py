# Secure Login System (Decorators)


def login_required(func):
    def wrapper():
        logged_in = True

        if logged_in:
            print("Login Successful")
            func()
        else:
            print("Please Login First")

    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard()
