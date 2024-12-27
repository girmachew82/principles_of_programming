value = None
result = value or 10
print(f"Since the value is {value} default is {result}")  # Output: default value is 10


value = None
result = value if value is not None else 15
print(f"Since the value is {value} default is {result}")  # Output: default is 15
