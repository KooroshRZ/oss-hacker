# Helper functions
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Time taken: {time.time() - start:.2f}s')
        return result
    return wrapper

