# Performance Tracker (Decorators)


import time

def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        print("Execution Time:", round(end - start, 5), "seconds")

    return wrapper

@calculate_time
def display():
    time.sleep(1)
    print("Program Executed")

display()
