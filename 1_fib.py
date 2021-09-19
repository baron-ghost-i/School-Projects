def fib(n: int) -> int:
    try:
        assert n > 0
    except AssertionError:
        raise ValueError("Value of input must be greater than 0")
    else:
        i = 1
        val1, val2 = 0, 1
        while i < n:
            val1, val2 = val2, val1+val2
            i += 1
        return val1

n = input("Enter the number of term of the Fibonacci series to be displayed: ")

if n.endswith("1") and not n.endswith("11"):
    suffix = "st"
elif n.endswith("2")  and not n.endswith("12"):
    suffix = "nd"
elif n.endswith("3") and not n.endswith("13"):
    suffix = "rd"
else:
    suffix = "th"

try:
    n = int(n)
except ValueError:
    raise ValueError("Value of input must be a natural number")
else:
    out = fib(int(n))
    print(f"{n}{suffix} term of the Fibonacci series: {out}")