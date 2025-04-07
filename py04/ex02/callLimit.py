def callLimit(limit: int):
    """Paramaterized decorator"""
    count = 0

    def callLimiter(function):
        """Actual decorator"""
        def limit_function(*args: any, **kwds: any):
            """Logic for limiting the number of calls"""
            nonlocal count

            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            function()
        return limit_function
    return callLimiter


# def main():
#     @callLimit(3)
#     def f():
#         print("f()")
#
#     @callLimit(1)
#     def g():
#         print("g()")
#
#     for i in range(3):
#         f()
#         g()
#
#
# if __name__ == "__main__":
#     main()
