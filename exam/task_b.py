def retry(check, n_attempts=5):
    def retry_decorator(func):
        def new_func(*args, **kwargs):
            if ((n_attempts is None) or (n_attempts <= 0)):
                while True:
                    result = func(*args, **kwargs)
                    if check(result):
                        return result
            for i in range(n_attempts):
                result = func(*args, **kwargs)
                if check(result):
                    return result
            raise RuntimeError("Expired number of retries")
        return new_func
    return retry_decorator
