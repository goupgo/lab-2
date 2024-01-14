def addition(n):
    if n == 0:
        return 0
    else:
        return n + addition(n - 1)

result = addition(10)
print(f"Sum of numbers from 0 to 10:", result)




n = int(input('Number'))
res = n * (n + 1) / 2
print(res)
