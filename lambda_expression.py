# Lambda Expression
result = list(map(lambda x: x + 10, [1, 2, 3]))
print(result)

# List Comprehension
result = [n * 2 for n in range(1, 10+1) if n % 2 == 1]
print(result)
