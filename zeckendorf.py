import numpy as np

def zeckendorf(num):
    """
    Parameters
    ----------
    num: integer
        The integer that the user wants to decompose into its zeckendorf
        representation.

    Returns
    -------
    representation: list
        The numbers that sum up to equal n.
    """

    golden = (1 + np.sqrt(5)) / 2
    get_fib = lambda x: int((golden ** x - (-golden) ** (-x)) / np.sqrt(5))
    # Uses the rounding formula from Wikipedia.
    n = int((np.log(num * np.sqrt(5)) / np.log(golden)))
    fib = get_fib(n)
    if get_fib(n + 1) == num:
        return [get_fib(n + 1)]

    else:
        # Finds the largest fibonacci number that's smaller than num.
        fib = int((golden ** n - (-golden) ** (-n)) / np.sqrt(5))
        decompose = [fib]
        b = num - fib
        decompose += (zeckendorf(b))
        return decompose
