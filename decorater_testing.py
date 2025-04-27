import time  
import atexit

# examplpe of a decorator as a function
def print_timing(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        print(f"Start:\t{start}")
        result = func(*args, **kwargs)
        end = time.time_ns()
        print(f"End:\t{time.time_ns()}")
        print(f"Duration:\t{end - start}")
        return result
    return wrapper

# example of a decorator as a class
class limit_calls:
    def __init__(self, limit):
        self.limit = limit
        self.calls = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.calls += 1
            if self.calls > self.limit:
                print(f"Function {func.__name__} has been called too many times.")
                return None
            result = func(*args, **kwargs)
            return result
        return wrapper

@limit_calls(2)
@print_timing
def add_up(a, b):
    return a + b

@atexit.register
def termination_function():
    print("Python script exits now!")

if __name__ == "__main__":
    print(add_up(1, 2))
    print(add_up(3, 4))
    print(add_up(3, 4))
