from time import perf_counter

def timeit(func):
    """
    Calculates the time that it took for the given function
    to execute. In seconds
    """
    def timeit_inner(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        time_taken = perf_counter() - start_time
        # if len(kwargs) > 0 and len(args) > 0:
        #     print(f"Function: {func.__name__}({args} {kwargs}) \
        #     Took {time_taken:.4f} seconds")
        # elif len(kwargs) == 0 and len(args) > 0:
        #     print(f"Function: {func.__name__}({args}) \
        #     Took {time_taken:.4f} seconds")
        # elif len(kwargs) > 0 and len(args) == 0:
        #     print(f"Function: {func.__name__}({kwargs}) \
        #     Took {time_taken:.4f} seconds")
        print(f"Function: {func.__name__}() \
        Took {time_taken:.4f} seconds")
        return result
    return timeit_inner
