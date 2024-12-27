global_var = 10

def func():
    global global_var
    global_var = 20
    return global_var

print(func())
print(global_var)